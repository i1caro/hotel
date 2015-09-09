from flask import Flask
from flask.ext.pymongo import PyMongo

app = Flask('hotel')
app.debug = True

mongo = PyMongo(app)
