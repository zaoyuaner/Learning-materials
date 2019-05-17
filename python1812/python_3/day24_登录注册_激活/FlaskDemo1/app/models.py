from app.ext import db


class Cat(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100))
    color = db.Column(db.String(40))
    age = db.Column(db.Integer)


# 字母模型类
# 一个字母 对应 多个城市
class Letter(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(4))
    # 声明
    citys = db.relationship('City', backref='letter', lazy=True)


# 字母模型类
class City(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    parentId = db.Column(db.Integer)
    regionName = db.Column(db.String(40))
    cityCode = db.Column(db.Integer)
    pinYin = db.Column(db.String(40))

    # 声明关系
    letter_id = db.Column(db.Integer, db.ForeignKey(Letter.id))


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(256))
    email = db.Column(db.String(20), unique=True)
    permissions = db.Column(db.Integer, default=1)
    icon = db.Column(db.String(256), default='atom.png')
    isactive = db.Column(db.Boolean, default=False)
    isdelte = db.Column(db.Boolean, default=False)