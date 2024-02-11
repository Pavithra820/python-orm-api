from app import db

class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(80),unique=False,nullable=False)
    password = db.Column(db.String(80),unique=False,nullable=False)
    email = db.Column(db.String(80),unique=True,nullable=False)
    mobile=db.Column(db.String(12),unique=True,nullable=False)
    city=db.Column(db.String(120),unique=False,nullable=False)
    designation=db.Column(db.String(10),nullable=False)

 