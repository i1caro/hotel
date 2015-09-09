from bs4 import BeautifulSoup


def hotel_items(html_doc):
    return BeautifulSoup(html_doc, 'html.parser').findAll(
        'div', {'class': 'sr_item_content'}
    )


def parse_item(hotel):
    try:
        price = hotel.find('td', {'class': 'roomPrice'}).text.strip()[2:]
    except AttributeError:
        price = None

    return {
        'name': hotel.a.text.strip(),
        'link': hotel.a.get('href').split('?')[0],
        'score': hotel.find('span', {'class': 'average'}).text,
        'price': price,
        'currency': 'EUR'
    }


def parser(html_doc):
    return [
        parse_item(hotel_item) for hotel_item in hotel_items(html_doc)
    ]
