1、RuntimeError 
错误地址： session['username'] = 'coco'   未加密
RuntimeError: The session is unavailable because no secret key was set.  Set the secret_key on the application to something unique and secret.
解决方法： 加密  app.secret_key = 'asfda8r9q3y9qy$#%GFSD^%W$TAfasdfasqwe'  # 加密方式（密钥种子）

2、redis.exceptions.ConnectionError
错误 ：redis 服务器未开启
redis.exceptions.ConnectionError: Error 111 connecting to 127.0.0.1:6379. Connection refused.
解决方法： 打开终端输入 redis-server

3、werkzeug.routing.BuildError
错误 ：反向解析路由传参的参数名不对
werkzeug.routing.BuildError: Could not build url for endpoint 'first.art' with values ['d']. Did you forget to specify values ['id']?
解决方法：改一下反向解析后面的参数名即可

4、werkzeug.routing.BuildError
错误 ： 反向解析过程中蓝图指向方法不一致
werkzeug.routing.BuildError: Could not build url for endpoint 'first.art' with values ['id']. Did you mean 'first.art1' instead?
解决方法：反向解析函数名和跳转页面定义的函数名一致

5、ValueError: urls must start with a leading slash
错误：子域名设置问题
解决方法：注意路由中引号内的斜线/不能缺少  url_prefix='/app'

6、sqlalchemy.exc.IntegrityError: (pymysql.err.IntegrityError) (1062, "Duplicate entry 'xiaoming' for key 'name'")
[SQL: INSERT INTO stuf1 (name, age) VALUES (%(name)s, %(age)s)]
[parameters: {'age': 18, 'name': 'xiaoming'}]
(Background on this error at: http://sqlalche.me/e/gkpj)
错误：重复添加不可重复数据
解决方法：注意唯一字段

7、sqlalchemy.orm.exc.UnmappedInstanceError
sqlalchemy.orm.exc.UnmappedInstanceError: Class 'builtins.list' is not mapped
错误：未标明的实例错误，添加数据内容写错了all_stus.append(stu)  错误时候写的是括号内（all_stus）
解决方法： 注意后台代码的准确性

8、TypeError
TypeError: not_() takes 1 positional argument but 2 were given
错误：flask框架中查询时，非not_，的参数是能有一个
解决方法：not_放在一个需要修饰的参数前面

9、AssertionError
 View function mapping is overwriting an existing endpoint function: blue.hello
错误：视图函数路径指向有问题

10、sqlalchemy.exc.NoForeignKeysError
sqlalchemy.exc.NoForeignKeysError: Could not determine join condition between parent/child tables on relationship Grade.stus - there are no foreign keys linking these tables.  Ensure that referencing columns are associated with a ForeignKey or ForeignKeyConstraint, or specify a 'primaryjoin' expression.
错误：定义模型类时关联字段有问题
解决方法：ForeignKey('grade_id')   => ForeignKey('grade.id')   分清关联的是谁的哪个字段在sql语句中和Python中的不同写法

11、AttributeError: type object 'Integer' has no attribute '_set_parent_with_dispatch'
错误原因：模型类书写错误
解决方法：db.Column('s_id'),db.Integer,db.ForeignKey('stu.id')) => db.Column('s_id',db.Integer,db.ForeignKey('stu.id'))   把括号位置写对

12、# relationship为关联关系，backref为反向引用
    stus = db.relationship('Student', backref='g')
错误: 移除数据，调用remove方法，当数据不存在的时候报错
解决方法：使用异常处理  try ... except


