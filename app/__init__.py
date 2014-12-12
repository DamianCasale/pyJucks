import os

from flask import Flask
from jinja2 import ChoiceLoader, FileSystemLoader

app = Flask(__name__)

base_dir = os.path.dirname(os.path.realpath(__file__))

app.jinja_loader = ChoiceLoader([FileSystemLoader(os.path.join(base_dir, 'static', 'templates'))]);

import routes