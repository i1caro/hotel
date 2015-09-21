import logging
from datetime import date
from datetime import datetime
from datetime import timedelta

from celery.schedules import crontab

from config.main import mongo, celery
from spiders.booking.runner import get

celery.conf.update(
    CELERYBEAT_SCHEDULE={
        'every-minute': {
            'task': 'periodic.tasks.every_four_hours',
            'schedule': crontab(minute='*/1'),
        },
    }
)


@celery.task
def every_four_hours():
    logging.info('Checking prices')
    for day in range(30):
        data = get(
            date.today() + timedelta(days=day),
            date.today() + timedelta(days=day + 1)
        )
        data.update(dict(
            time=datetime.now(),
            date_requested=date.today() + timedelta(days=day)
        ))
        mongo.db.faro_prices.insert(data)
