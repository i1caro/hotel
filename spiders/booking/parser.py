from bs4 import BeautifulSoup
import logging


def log_on_error(func):
    def safe_function(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception as e:
            logging.ERROR(
                'Error {} while parsing {} {} {}'.format(e, func, args, kwargs)
            )
    return safe_function


@log_on_error
def hotel_items(html_doc):
    return BeautifulSoup(html_doc, 'html.parser').findAll(
        'div', {'class': 'sr_item_content'}
    )


@log_on_error
def parse_item(hotel):
    try:
        currency, _, price = hotel.find(
            'td', {'class': 'roomPrice'}
        ).text.strip()
    except Exception:
        price = None,
        currency = None

    return {
        'name': hotel.a.text.strip(),
        'link': hotel.a.get('href').split('?')[0],
        'score': hotel.find('span', {'class': 'average'}).text,
        'price': price,
        'currency': currency
    }


def parser(html_doc):
    return [
        parse_item(hotel_item) for hotel_item in hotel_items(html_doc)
    ]
