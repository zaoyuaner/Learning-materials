## 虚拟环境
### virtualenv
- 安装：pip install virtualenv
- 创建虚拟环境：建议环境代码分离
  virtualenv --no-site-packages -p python.exe的路径(盘符开始) env_name
- 进入虚拟环境
  Windows下：activate          Mac/Ubuntu：source activate
- 退出虚拟环境：deactivate
### Python3下的venv
  创建命令：python -m venv env_name

## flask应用
> flask项目的应用过程中需要进行代码优化、项目拆分，第一个问题是避免循环导包
### 启动方式
- 第一种启动方式
  直接启动，host、port、debug参数写在run函数中
- 第二种启动方式
  通过sys库，获取sys.args的下标为1、2的参数，启动
- 第三种启动方式
  通过flask-script插件，实例化Manager对象启动
  安装flask-script：pip install flask-script
  导包：from flask-script import Manager
  管理：manager = Manager(app)
  调用：manager.run()
  启动：python manage.py(应用名) runserver -p 端口 -h ip地址 -d（debug模式）
### 路由规则
- 写法：@app.route('/index/<int:id>/')
- 格式：<转换器：参数名>
- 常用转换器类型：string(默认)、int、float、uuid、path等
### 请求request
- get取值
  request.args[key]
  request.args.get(key)
  request.args.getlist(key)
- post取值
  request.form
- 文件
  request.files
- 请求方法
  request.method
- 路由地址
  request.path
- cookies
  request.cookies
### 响应response
**cookie**
- 情况1：可以直接返回响应内容
- 情况2：创建响应对象
  res = make_respone(响应内容，状态码-默认值200)
  设置cookie：res.set_cookie(key,value,max_age)
  删除cookie：res.delete_cookie(key)
**session**

### cookie/session
- flask默认的session使用方式
  数据存储在cookie中
- flask-session插件指定存储数据库（一般使用redis）
  **配置redis数据库：**
  1、设置秘钥种子：app.secret_key='sdfdsfafdasdfadsfasdfasd随便写'
  2、设置数据库：SESSION_TYPE='redis'
  3、连接数据库：SESSION_REDIS= redis.Redis(host,port)

### 装饰器
- 条件：
  1、外层函数嵌套内层函数
  2、外层函数的返回值是内层函数
  3、内层函数调用外层函数
- wraps函数
  作用：保留原函数的的属性
  使用：导入functools   通过语法糖修饰内层函数

### 蓝图
- 作用：代替应用管理路由，用于优化项目，项目代码块拆分
- 使用
  安装：pip install flask-blueprint
  实例化蓝图：blue = Blueprint('蓝图名', __name__) #蓝图名随便写一般用blue就可以，可以用于反向解析
  注册蓝图：flask对象名.resgister_blueprint(blueprint=blue, url_prefix='/xxx')  url_prefix指定路由的起始位置，斜线记得写
  使用蓝图管理路由： @blue.route('/')
- 跳转 redirect
  1、无参情况：
    redirect('/app/home/')   指定路由
    redirect(url_for(blue(生成蓝图指定的名称).跳转的函数名))    反向在解析的写法
  2、有参情况：
    redirect('/app/home/12/')
    redirect(url_for('blue.跳转函数名', 参数名=值,...,参数名n=值n))

### 模板
- 指定模板位置
```
  manage.py中
  参数__name__表示flask以哪个模块所在目录当做项目的根目录，项目根目录中默认static为静态目录，templates为模板目录
  app = Flask(__name__,  # 如果指定的__name__模块没有找到,会把当前模块所在目录当成项目根目录。
            static_url_path="/static",  # 访问静态资源的url前缀, 默认值是static
            static_folder="static",  # 静态文件的存放目录，默认就是static
            template_folder="templates",  # 模板文件的目录，默认是templates
            )
```
- 语法：就是HTML语言在模板中的写法
```
  - 变量 {{ 变量名 }}

  - 标签 {% 标签 %} {% end标签名 %}
  - 标签的使用
  填坑标签：{% block 名称 %} 填充内容 {% endblock %}
  if标签：
  {% if 条件 %} {% else %} {% endif %}
  for标签：
  {% for i in a %} {% else %} {% endfor %}
    显示效果：
        从1开始编号：{{ loop.index }}
        从0开始编号：{{ loop.index0 }}
        倒序到1结束：{{ loop.revindex }}
        倒序到0结束：{{ loop.revindex0 }}
        第一次循环返回True：{{ loop.first }}
        最后一次循环返回True：{{ loop.last }}

  - 过滤器
  解析变量中的样式：{{ 变量 | safe}}
  删除变量中的样式：{{ 变量 | striptags }}
  
```
- 继承
  写法：{% extends '模板位置（如'base.html'）'%}
  父模板挖坑：定义一个能被子模板继承的父模板，父模板中需定义block块，block块是被动态填充的部分
  子模板填坑：继承父模板，并动态的填充block块中的内容
- 扩展
  include标签

### 模型的基础用法
- 创建数据库对象
  安装：pip install flask-sqlalchemy
  创建对象：models.py => db = SQLAlchemy()
  配置数据库连接信息：
  manage.py => 
    app.config[SQLALCHEMY_DATABASE_URI]='数据库名+驱动（如pymysql）://mysql用户名：密码@数据库主机ip：端口/数据库名'
    数据库手动去MySQL中添加。
  初始化对象：manage.py => db.init_app(Flask对象如app)
- 定义模型
```
  - 字段类型
    整形：Integer   默认长度11位
    varchar类型：String(size)
    布尔类型：Boolean
    日期类型：Datetime
    长文本类型：Text
    浮点型：Float
  - 字段约束
    是否唯一：unique=True/Flase
    是否为空：nullable
    设置主键：primary_key
    设置默认值：default
  - 设置表名
    __tablename__=表名  不写的话，表名就是模型类的小写
```
- 使用模型 (模型类名.query.方法())
```
  - 迁移产生数据库表（只有第一次执行有效，表存在不生效）
    create_all()
  - 删除
    drop_all()

  - 增
    db.session.add(对象)
    db.session.add_all(对象列表)
    db.session.commit()
  - 删
    db.session.delete(对象)
    db.session.commit()
  - 改
    db.session.add(对象)——这一句可以不写,直接提交
    db.session.commit()
> 增删改的这两行代码可以简写为一条命令，在models重新定义方法即可
  - 查
    - 精准查询
      filter_by(字段=值)   #只能用于精准查询
      filter（模型名.字段 == 值）
      查询主键所在行的数据：get(主键)
    - 排序 
      升序 order_by(模型名.字段)
      降序 order_by(-模型名.字段)
    - 分页
      跳过几个参数再截取几个参数：offset().limit()
    - 模糊查询
      包含=like ‘%a%’： contains()
      以什么开头=like "%xiaoming"   startswith
      以什么结尾=like "xiaomign%"   endswith
      第几位是什么= like '_a'       like()
    - 且 或 非
      and_(一般用逗号代替)
      or_()
      not_()  只能有一个参数
    - 大于  小于  大于等于   小于等于
      可以直接用符号写  >  <   >=   <=
      也可以用字母表示 __gt__ 等  
```

### 模型的高级用法
**级联关系**
- 一对多
- 多对多

> relationship可以定义在任何模型的任何一方






































