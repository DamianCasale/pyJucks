import os

from flask import Flask
from jinja2 import ChoiceLoader, FileSystemLoader

import zerorpc

zClient = zerorpc.Client()
zClient.connect("tcp://127.0.0.1:11110")

app = Flask(__name__)

import routes