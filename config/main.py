import os

from flask import Flask
from flask.ext.pymongo import PyMongo

from config.logging import *
from config.celery import celery_config, make_celery

app = Flask('hotel')

app.debug = os.environ.get('HOTEL_DEBUG', False)

mongo = PyMongo(app)

app.config.update(
    celery_config
)
celery = make_celery(app)
