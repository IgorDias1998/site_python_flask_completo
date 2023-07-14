from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)


app.config['SECRET_KEY'] = '84c8d62895eb539ef7f44fe1289b3b2a'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projeto.db'
bancodedados = SQLAlchemy(app)

bcrypt = Bcrypt(app)
loginmanager = LoginManager(app)
loginmanager.login_view = 'login'
loginmanager.login_message_category = 'alert-info'

from siteCompleto import routes