from flask import Flask
# from flask_restful import  Api

from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

db=SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['JWT_SECRET_KEY']="HS256"
    app.config["SQLALCHEMY_DATABASE_URI"]= "mysql+pymysql://root:experion%40123@localhost/contact"
    
    db.init_app(app)        # to get the dbs collection instance
    jwt = JWTManager(app)
    from app.user import user_bp
    app.register_blueprint(user_bp)
    
    return app


