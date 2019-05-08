from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from logging.handlers import SMTPHandler
import logging
from flask_mail import Mail

app = Flask(__name__)

from flask_blog.configuration import Config
app.config.from_object(Config)

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
mail = Mail(app)

from flask_blog import routes

# if True:
#     if app.config['MAIL_SERVER']:
#         auth = None
#         if app.config['MAIL_USERNAME'] or app.config['MAIL_PASSWORD']:
#             auth = (app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])
#         secure = None
#         if app.config['MAIL_USE_TLS']:
#             secure = ()
#         mail_handler = SMTPHandler(
#         mailhost=(app.config['MAIL_SERVER'], app.config['MAIL_PORT']),
#         fromaddr='no-reply@'+app.config['MAIL_SERVER'],
#         toaddrs=app.config['ADMINS'],
#         subject='Flask Blog Crash',
#         credentials=auth,
#         secure=secure)
#         mail_handler.setLevel(logging.DEBUG)
#         app.logger.addHandler(mail_handler)
