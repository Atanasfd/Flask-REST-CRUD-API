from app import db

class Contact(db.Model):
    id = db.Column(db.Integer,primary_key= True)
    UserName = db.Column(db.String(32),index=True,unique=True)
    FirstName = db.Column(db.String(64))
    SurName = db.Column(db.String(64))
    phone = db.Column(db.Integer())

