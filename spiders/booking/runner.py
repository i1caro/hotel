import requests

from spiders.booking.parser import parser

url = 'http://www.booking.com'
prices_url = url + '/searchresults.html'

get_params = [
    ('city', '-2165075'),  # important
    ('class_interval', '1'),
    ('csflt', '%7B%7D'),
    ('dtdisc', '0'),
    ('group_adults', '2'),
    ('group_children', '0'),
    ('hlrd', '0'),
    ('hyb_red', '0'),
    ('inac', '0'),
    ('label_click', 'undef'),
    ('nha_red', '0'),
    ('no_rooms', '1'),  # important
    ('offset', '0'),
    ('redirected_from_city', '0'),
    ('redirected_from_landmark', '0'),
    ('redirected_from_region', '0'),
    ('review_score_group', 'empty'),
    ('room1', 'A%2CA'),
    ('sb_price_type', 'total'),
    ('score_min', '0'),
    ('si', 'ai%2Cco%2Cci%2Cre%2Cdi'),
    ('src', 'searchresults'),
    ('ss', 'Faro'),
    ('ss_all', '0'),
    ('ssb', 'empty'),
    ('sshis', '0'),
    ('ssne', 'Faro'),
    ('ssne_untouched', 'Faro'),
    ('rows', '1000'),  # important
    ('selected_currency', 'EUR'),  # important
]

headers = {
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Accept': (
        'text/html,application/xhtml+xml,application/xml;q=0.9,'
        'image/webp,*/*;q=0.8'
    ),
    'Cache-Control': 'no-cache',
    'Accept-Language': 'en-US,en;q=0.8,pt-PT;q=0.6,pt;q=0.4,en-GB;q=0.2',
    'User-Agent': (
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like '
        'Gecko) Ubuntu Chromium/44.0.2403.89 Chrome/44.0.2403.89 Safari/537.36'
    ),
    'HTTPS': '1',
    'Accept-Encoding': 'gzip, deflate, sdch',
}


def start_params(start):
    return [
        ('checkin_monthday', start.day),
        ('checkin_year_month', '{}-{}'.format(start.year, start.month)),
    ]


def end_params(end):
    return [
        ('checkout_monthday', end.day),
        ('checkout_year_month', '{}-{}'.format(end.year, end.month)),
    ]


def get(start, end):
    first_call = requests.get(
        url=url,
        headers=headers
    )
    response = requests.get(
        url=prices_url,
        cookies=first_call.cookies,
        headers=headers,
        params=(start_params(start) + end_params(end) + get_params)
    )
    return parser(response.text)


if __name__ == '__main__':
    print(get())
