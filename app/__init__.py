import os

from flask import Flask
from jinja2 import ChoiceLoader, FileSystemLoader

app = Flask(__name__)

import routes
