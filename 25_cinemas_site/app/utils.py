import os
import requests
import urllib.parse

from bs4 import BeautifulSoup
from threading import Thread
from werkzeug.contrib.cache import SimpleCache

CACHE = SimpleCache()
CACHE_TIMEOUT = 60 * 60
REQUEST_TIMEOUT = 2


AFISHA_PAGE_URL = 'https://www.afisha.ru/msk/schedule_cinema/'
KINOPOISK_INDEX_PAGE_URL = 'https://kinopoisk.ru/index.php'
KINOPOISK_START_PAGE_URL = 'https://www.kinopoisk.ru'
HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'ru,en-us;q=0.7,en;q=0.3',
    'Accept-Encoding': 'UTF-8',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.2 Safari/605.1.15',
    'Accept-Charset': 'windows-1251,utf-8;q=0.7,*;q=0.7',
    'Keep-Alive': '300',
    'Connection': 'keep-alive',
    'Referer': KINOPOISK_START_PAGE_URL
}

STATIC_FOLDER = '../static/img/'


def fetch_site_page(site_url, headers, payload=None):
    identifier = site_url
    if payload:
        identifier = payload.get('kp_query')
    site_page = CACHE.get(identifier)
    if site_page:
        return site_page

    site_page = requests.get(
        site_url,
        params=payload,
        headers=headers
    ).text
    CACHE.set(identifier, site_page, timeout=CACHE_TIMEOUT)
    return site_page


def parse_afisha_list(raw_html):
    soup = BeautifulSoup(raw_html, 'html.parser')
    movies_markup = soup.findAll('a', class_='card__link', href=True)
    movies_data = []
    for movie in movies_markup:
        movie_data = dict()
        movie_data['link'] = movie['href'].strip()
        movie_data['title'] = movie.find(
            'h3', class_='card__title'
        ).text.strip()
        movies_data.append(movie_data)
    return movies_data


def get_movies_list():
    afisha_page_html = fetch_site_page(AFISHA_PAGE_URL, HEADERS)
    return parse_afisha_list(afisha_page_html)


def get_movie_threads(movies_list):
    movie_threads = []
    for movie in movies_list:
        movie_title = movie.get('title')
        movie_afisha_link = movie.get('link')
        payload = {'first': 'yes', 'kp_query': movie_title}
        movie_thread = MovieThread(
            KINOPOISK_INDEX_PAGE_URL,
            HEADERS,
            payload
        )
        movie_thread.set_movie_afisha_link(movie_afisha_link)
        movie_thread.start()
        movie_threads.append(movie_thread)
    for movie_thread in movie_threads:
        movie_thread.join()
    return movie_threads


def get_composed_movie_instances(movie_threads):
    movies = [
        Movie(
            x.movie_data['title'],
            x.movie_data['afisha_link'],
            x.movie_data['html']
        ) for x in movie_threads]
    for movie in movies:
        movie.record_rating()
        movie.record_reviews_amount()
        movie.record_poster_link()
    return movies


class MovieThread(Thread):
    def __init__(self, url, headers, payload):
        super().__init__()
        self.url = url
        self.headers = headers
        self.payload = payload
        self.movie_data = dict()

    def run(self):
        kinopoisk_page_html = fetch_site_page(
            self.url,
            self.headers,
            self.payload
        )
        self.movie_data['html'] = kinopoisk_page_html
        self.movie_data['title'] = self.payload.get('kp_query')

    def set_movie_afisha_link(self, movie_afisha_link):
        self.movie_data['afisha_link'] = movie_afisha_link


class Movie:
    def __init__(self, title, movie_afisha_link, movie_kinopoisk_html):
        self.title = title
        self.movie_afisha_link = movie_afisha_link
        self.kinopoisk_html = movie_kinopoisk_html
        self.rating = float('-inf')
        self.reviews_amount = 'Failed to get reviews amount'
        self.poster_link = STATIC_FOLDER + 'not-found.png'

    def record_rating(self):
        soup = BeautifulSoup(self.kinopoisk_html, 'html.parser')
        rating = soup.find('span', class_='rating_ball')
        try:
            self.rating = float(rating.text)
        except (ValueError, TypeError, AttributeError) as e:
            pass

    def record_reviews_amount(self):
        soup = BeautifulSoup(self.kinopoisk_html, 'html.parser')
        reviews_amount = soup.find('span', class_='ratingCount')
        if reviews_amount:
            self.reviews_amount = reviews_amount.text
        else:
            pass

    def record_poster_link(self):
        soup = BeautifulSoup(self.kinopoisk_html, 'html.parser')
        try:
            poster_path_a = soup.select('.popupBigImage')[0].get('onclick')
            poster_path = poster_path_a[
                          poster_path_a.find("'")+1:poster_path_a.rfind("'")
                          ]
            self.poster_link = urllib.parse.urljoin(
                KINOPOISK_START_PAGE_URL, poster_path
            )
        except (IndexError, ):
            pass
