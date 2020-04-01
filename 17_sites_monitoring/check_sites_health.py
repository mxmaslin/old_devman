import datetime
import pytz
import requests
import whois
from argparse import ArgumentParser


def get_console_args():
    parser = ArgumentParser(description='Get file with urls')
    parser.add_argument('urls_file_path', help='Path to urls containing file')
    parser.add_argument(
        'period_of_interest',
        type=int,
        nargs='?',
        default=30,
        help='Whether the site paid more than this n days'
    )
    return parser.parse_args()


def load_urls4check(path):
    try:
        with open(path) as file:
            urls_list = [url.strip() for url in file.readlines()]
            return urls_list
    except FileNotFoundError:
        return None


def get_expiration_date(domain_name):
    whois_data = whois.whois(domain_name)
    expiration_date = whois_data.expiration_date
    if isinstance(whois_data.expiration_date, list):
        expiration_date = expiration_date[0]
    return expiration_date


def is_response_ok(url):
    try:
        response = requests.get(url)
        return response.ok
    except (requests.exceptions.MissingSchema,
            requests.exceptions.ConnectionError
            ):
        return None


def get_response_status_message(response_ok):
    if response_ok:
        return 'responded with HTTP 200.'
    if response_ok is None:
        return 'was not found.'
    return 'did not respond with HTTP 200.'


def get_days_until_expiration(expiration_date):
    try:
        expiration_dt_tz_aware = expiration_date.replace(tzinfo=pytz.UTC)
        now = datetime.datetime.now().replace(tzinfo=pytz.UTC)
        return (expiration_dt_tz_aware - now).days
    except (ValueError, AttributeError):
        return None


def get_expiration_date_message(period_of_interest, days_until_expiration):
    if days_until_expiration:
        if period_of_interest > days_until_expiration:
            return 'Domain is payed less than period of interest'
        return 'Domain is payed longer than period of interest'
    return 'Expiration date not found.'


def get_site_health_message(
        url, response_ok, period_of_interest, days_until_expiration
):
    response_status_message = get_response_status_message(response_ok)
    expiration_date_message = get_expiration_date_message(
        period_of_interest, days_until_expiration
    )
    return ' '.join([url, response_status_message, expiration_date_message])


if __name__ == '__main__':
    args = get_console_args()
    file_path = args.urls_file_path
    period_of_interest = args.period_of_interest
    urls4check = load_urls4check(file_path) or exit('File not found')
    for url in urls4check:
        response_ok = is_response_ok(url)
        expiration_date = get_expiration_date(url)
        days_until_expiration = get_days_until_expiration(expiration_date)

        print(
            get_site_health_message(
                url, response_ok, period_of_interest, days_until_expiration
            )
        )
