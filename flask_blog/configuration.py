import os
from flask_blog import app


class Config():
    app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
    #some
    #app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
    DB_USERNAME = "root"
    DB_PASSWORD = "root"
    BLOG_DATABASE_NAME = 'blog_db'

    app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@mysql:3306/{BLOG_DATABASE_NAME}"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['DEBUG'] = True
    app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USERNAME'] = 'pythontestemailshtrikuldmitry'
    app.config['MAIL_PASSWORD'] = 'contango90'
    app.config['ADMINS'] = ['dmitriyshtrikul@gmail.com']
