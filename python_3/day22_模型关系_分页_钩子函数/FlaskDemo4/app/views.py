import random
import uuid

from flask import Blueprint, render_template, redirect, url_for, request, g, session
from app.models import User, Grade, Student, Goods, UserModel
from app.ext import db, cache

blue = Blueprint('blue', __name__)

def init_view(app):
    app.register_blueprint(blueprint=blue)


@blue.route('/')
def hello_world():

    # 设置
    cache.set('username', 'atom', timeout=60)

    return render_template('index.html')


@blue.route('/adduser/')
def adduser():
    user = User()
    user.name = str(random.randrange(10000)) + 'xxx'
    user.score = random.randrange(1,100)

    db.session.add(user)
    db.session.commit()

    return '创建成功'

@blue.route('/deluser/')
def deluser():
    user = User.query.first()

    db.session.delete(user)
    db.session.commit()

    return '删除'

@blue.route('/updateuser/')
def updateuser():
    user = User.query.first()
    user.name = '哈哈'

    db.session.add(user)
    db.session.commit()

    return '更新'


@blue.route('/selecctuser/')
def selecctuser():
    users = User.query.all()

    # id > 3
    # users = User.query.filter(User.id > 3)
    # id == 3
    # users = User.query.filter(User.id== 3)

    # users = User.query.filter(User.name.startswith('7'))
    # users = User.query.filter(User.name.endswith('x'))
    # users = User.query.filter(User.name.contains('8'))

    # users = User.query.filter(User.id.in_([3,5,7]))

    # users = User.query.filter(User.id > 4).filter(User.score > 40)

    # users = User.query.filter(User.score > 60).limit(1)

    # users = User.query.order_by(-User.score)

    users = User.query.offset(5)

    return render_template('selecctuser.html', users=users)


@blue.route('/getuser/')
def getuser():
    # pk
    user = User.query.get(3)

    return '用户: ' + user.name



@blue.route('/addgrade/')
def addgrade():
    grade = Grade()
    grade.name = 'Python19{}'.format(random.randrange(10,100))

    db.session.add(grade)
    db.session.commit()

    return render_template('grade.html', grade=grade)

@blue.route('/showgrade/')
def showgrade():
    grades = Grade.query.all()

    return render_template('showgrade.html', grades=grades)


@blue.route('/gradedetail/<int:gradeid>/')
def gradedetail(gradeid):

    grade = Grade.query.get(gradeid)
    # 方式一: 直接过滤
    students = Student.query.filter(Student.grade_id == gradeid)

    # 方式二: 级联

    return render_template('grade.html', grade=grade, students=students)


@blue.route('/addstudent/<int:gradeid>/')
def addstudent(gradeid):
    student = Student()
    student.name = str(random.randrange(1000)) + '-张三'
    student.score = random.randrange(1, 100)

    # 设置班级
    student.grade_id = gradeid

    db.session.add(student)
    db.session.commit()

    print('添加的这个学生对应班级人数: ' + str(len(student.grade.students)))

    # 班级
    grade = Grade.query.get(gradeid)
    # 方式二: 级联

    return render_template('grade.html', grade=grade, students=grade.students)


# @blue.route('/home/')
# @blue.route('/home/<int:num>/')
# def home(num=1):
#
#     # goods_list = Goods.query.all()
#
#     # 根据页码获取对应的数据
#     # 每页显示20条数据
#     # goods_list = Goods.query.offset(20*(num-1)).limit(20)
#
#
#     # 系统自带的分页器
#     paginate = Goods.query.paginate(num, 20)
#
#
#     # 1,2,None,13,14,15,16,17,18,19,20,None,32,33
#
#     return render_template('home.html', paginate=paginate, total_num=range(1,paginate.pages+1))



@blue.route('/home/')
# @cache.cached(timeout=30)
def home():
    # print(g.ip)
    # print(g.name)

    # token = session.get('token')
    # users = UserModel.query.filter(UserModel.token == token)
    # if users.count():
    #     user = users.first()
    # else:
    #     user = None

    num = int(request.args.get('page', '1'))

    # 系统自带的分页器
    paginate = Goods.query.paginate(num, 20)

    # 1,2,None,13,14,15,16,17,18,19,20,None,32,33

    return render_template('home1.html', paginate=paginate, user=g.user)




# 钩子函数
# @blue.before_request
# def beforeView():
#     ip = request.remote_addr
#
#     # 缓存中获取
#     value = cache.get(ip)
#
#
#     g.ip = ip
#     g.name = 'atom'
#
#     if value:   # 爬虫，不给请求
#         return '小伙子，你有点过火了哈，爬我的数据!'
#
#     # 添加缓存
#     cache.set(ip, '爬虫', timeout=10)



###
@blue.before_request
def beforeView():
    token = session.get('token')
    users = UserModel.query.filter(UserModel.token == token)
    if users.count():
        g.user = users.first()
    else:
        g.user = None


@blue.route('/register/', methods=['POST'])
def register():
    user = UserModel()
    user.username = request.form.get('username')
    user.password = request.form.get('password')
    user.token = uuid.uuid5(uuid.uuid4(), 'register').hex
    db.session.add(user)
    db.session.commit()

    # 状态保持
    session['token'] = user.token

    return redirect(url_for('blue.home'))


@blue.route('/logout/')
def logout():
    session.pop('token')
    return redirect(url_for('blue.home'))

@blue.route('/login/', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    users = UserModel.query.filter(UserModel.username == username).filter(UserModel.password == password)
    if users.count():
        user = users.first()
        user.token = uuid.uuid5(uuid.uuid4(), 'register').hex
        db.session.add(user)
        db.session.commit()

        # 状态保持
        session['token'] = user.token

        return redirect(url_for('blue.home'))

    else:
        return '登录失败'



@blue.route('/cart/')
def cart():
    # token = session.get('token')
    # users = UserModel.query.filter(UserModel.token == token)
    # if users.count():
    #     user = users.first()
    # else:
    #     user = None

    return render_template('cart.html', user=g.user)


@blue.route('/about/')
def about():
    # token = session.get('token')
    # users = UserModel.query.filter(UserModel.token == token)
    # if users.count():
    #     user = users.first()
    # else:
    #     user = None

    return render_template('about.html', user=g.user)
