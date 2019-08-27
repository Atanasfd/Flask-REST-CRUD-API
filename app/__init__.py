from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


WTF_CSRF_ENABLED = True 
SECRET_KEY= "random password"


SQLALCHEMY_DATABASE_URI='sqlite:///:memory'


db = SQLAlchemy(app)

from app import views,models
db.create_all()
