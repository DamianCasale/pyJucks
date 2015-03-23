import os

from flask import Flask
from jinja2 import ChoiceLoader, FileSystemLoader
from celery import Celery
from pyRpc import PyRpc, RpcConnection

app = Flask(__name__)

'''
set up celery worker to talk to the logic layer.
return back as part of the app
'''
app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'
celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)

import routes