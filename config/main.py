from celery import Celery
from flask import Flask
from flask.ext.pymongo import PyMongo

from config.logging import *
from config.celery import celery_config, make_celery

app = Flask('hotel')
app.debug = True

mongo = PyMongo(app)

app.config.update(
    celery_config
)
celery = make_celery(app)
