from app.ext import db


class Wheel(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80))
    img = db.Column(db.String(256))


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(256))
    email = db.Column(db.String(255), unique=True)

class Goods(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(256))
    price = db.Column(db.String(100))
    img = db.Column(db.String(256))
