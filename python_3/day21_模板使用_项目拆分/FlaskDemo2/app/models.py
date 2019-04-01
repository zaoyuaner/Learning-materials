from app.ext import db


class User(db.Model):
    __tablename__ = 'app_user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80))
    password = db.Column(db.String(80))
