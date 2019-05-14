from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from logging.handlers import SMTPHandler
import logging
from flask_mail import Mail

app = Flask(__name__)

from flask_blog.configuration import Config
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app,db)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
mail = Mail(app)

from flask_blog import routes, models_db
