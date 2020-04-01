import json
import pytz
import requests
from datetime import datetime


def load_attempts():
    url = 'http://devman.org/api/challenges/solution_attempts'
    number_of_pages = requests.get(url).json()['number_of_pages']
    page = 1
    while True:
        payload = {'page': page}
        response = requests.get(url, params=payload)
        attempts = response.json()['records']
        for attempt in attempts:
            yield attempt
        page += 1
        if page > number_of_pages:
            break


def get_midnighters(attempts):
    morning_start = 4
    midnighters = set()
    for attempt in attempts:
        attempt_timestamp = attempt['timestamp']
        attempt_tz = pytz.timezone(attempt['timezone'])
        attempt_dt = datetime.fromtimestamp(attempt_timestamp, attempt_tz)
        attempt_hour = attempt_dt.hour
        attempt_username = attempt['username']
        if 0 <= attempt_hour < morning_start:
            midnighters.add(attempt_username)
    return midnighters


if __name__ == '__main__':
    attempts = load_attempts()
    midnighters = get_midnighters(attempts)
    for midnighter in midnighters:
        print(midnighter)
