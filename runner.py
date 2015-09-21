import logging

from flask import render_template
from config.main import app, mongo

# from config.main import celery

# @celery.task
# def add(x, y):
#     return x + y


@app.route('/')
def home_page():
    return render_template(
      'index.html', rows=mongo.db.faro_prices.find()
    )


@app.route('/fire_actions', methods=['GET'])
def fire_actions():
    logging.error('Fire in the hole')
    from periodic.tasks import every_four_hours
    every_four_hours()
    return render_template(
      'good.html'
    )


if __name__ == '__main__':
    app.run()
