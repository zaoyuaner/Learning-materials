from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    # 必须设置有主键
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))


class Student(db.Model):
    # 必须设置有主键
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), unique=True)
