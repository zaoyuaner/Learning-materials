
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# 用户类
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(255),nullable=False)
    is_delete = db.Column(db.Boolean, default=0)
    create_time = db.Column(db.DateTime, default=datetime.now())
    # 定义数据库表名
    __tablename__ = 'user'

    # 定义保存方法
    def save(self):
        db.session.add(self)
        db.session.commit()

# 一对多
# # 文章类型类（一）
class ArticleType(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 标题名称
    t_name = db.Column(db.String(30), unique=True,nullable=False)
    # 关联从表
    arts = db.relationship('Article', backref='tp')

    __tablename__ = 'art_type'

#
# # 文章类（多）
class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(30), unique=True, nullable=False)
    desc = db.Column(db.String(255), nullable=False)
    content = db.Column(db.TEXT, nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.now())
    # 通过外键声明关系
    type = db.Column(db.Integer,db.ForeignKey('art_type.id'))



# Terminal: python manage.py shell
# from back.models import db
# 创建模型对应表：db.create_all()




















