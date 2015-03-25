import os

from flask import Flask
from jinja2 import ChoiceLoader, FileSystemLoader

from flask.ext.login import LoginManager
from flask.ext.acl import ACLManager

app = Flask(__name__)

login_manager = LoginManager()
login_manager.login_view = "login"
login_manager.login_message = u"Please log in to access this page."
login_manager.refresh_view = "reauth"

login_manager.init_app(app)

app.secret_key = "yeah, not actually a secret"

# must be after app init
import routes