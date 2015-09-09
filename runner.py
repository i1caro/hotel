
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


@app.route('/get', methods=['GET'])
def get_faro_stuff():
    mongo.db.faro_prices.remove()
    from spiders.booking.runner import get

    return render_template(
      'inserted.html', inserted=mongo.db.faro_prices.insert(get())
    )


if __name__ == '__main__':
    app.run()
