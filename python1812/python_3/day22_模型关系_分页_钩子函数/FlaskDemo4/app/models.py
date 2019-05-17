from app.ext import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), unique=True)
    score = db.Column(db.Integer)


# 班级
# 一个班级 对应 多个学生
class Grade(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(40))

    # 对应的学生(不会生成字段，只是为了声明)
    # db.relationship('关系模型类', backref='当前模型表名')
    # db.relationship('关系模型类', backref='当前模型表名', lazy=True)
    students = db.relationship('Student', backref='grade', lazy=True)

# 学生
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(40))
    score = db.Column(db.Integer)

    # 添加关系
    # 但是后续使用的时候，也可以获取关联的对象!!!
    # student.grade.name
    grade_id = db.Column(db.Integer, db.ForeignKey(Grade.id))


# 商品模型类
class Goods(db.Model):
    # 商品id，主键
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 商品名称
    name = db.Column(db.String(20))
    # 商品图片
    icon = db.Column(db.String(255))
    # 商品价格
    price = db.Column(db.Integer)
    # 商品描述
    detail = db.Column(db.String(255))


class UserModel(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(256))
    token = db.Column(db.String(256))