import random
import requests

from bs4 import BeautifulSoup


AFISHA_PAGE_URL = 'https://www.afisha.ru/msk/schedule_cinema/'
KINOPOISK_PAGE_URL = 'https://kinopoisk.ru/index.php'
HEADERS = {
    'Accept-Encoding': 'UTF-8',
    'Accept-Language': 'Ru-ru',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.2 Safari/605.1.15',
}
NUM_MOVIES_TO_DISPLAY = 10
PROXIES_FILE = 'proxies.txt'
TIMEOUT = 3


def get_proxies_file(filename):
    with open(filename) as file:
        return file.read()


def get_proxies_list(file_contents):
    return file_contents.split()


def fetch_site_page(proxies, site_url, payload=None):
    for proxy in proxies:
        try:
            return requests.get(
                site_url,
                params=payload,
                headers=HEADERS,
                proxies={'https': proxy},
                timeout=TIMEOUT
            ).text
        except (requests.exceptions.ProxyError, ):
            continue
    return requests.get(
        site_url,
        params=payload,
        headers=HEADERS,
        timeout=TIMEOUT
    ).text


def parse_afisha_list(raw_html):
    soup = BeautifulSoup(raw_html, 'html.parser')
    movies_markup = soup.findAll('h3', class_='card__title')
    return [movie.text.strip() for movie in movies_markup]


def get_movie_score(movie_page):
    soup = BeautifulSoup(movie_page, 'html.parser')
    rating = soup.find('span', class_='rating_ball')
    try:
        rating = float(rating.text)
    except (ValueError, TypeError, AttributeError):
        rating = float('-inf')
    reviews_amount = soup.find('span', class_='ratingCount')
    if reviews_amount:
        reviews_amount = reviews_amount.text
    else:
        reviews_amount = 'No reviews are available'
    return rating, reviews_amount


def output_movies_to_console(movies):
    print()
    movie_data = "Name: {} rating: {} reviews: {}"
    for movie in movies:
        name, rating, reviews = movie.values()
        if rating == float('-inf'):
            rating = 'Rating is not available'
        print(movie_data.format(name, rating, reviews))


if __name__ == '__main__':
    proxies_file = get_proxies_file(PROXIES_FILE)
    proxies_list = get_proxies_list(proxies_file)
    afisha_page_html = fetch_site_page(proxies_list, AFISHA_PAGE_URL)
    movies_list = parse_afisha_list(afisha_page_html)[:NUM_MOVIES_TO_DISPLAY]
    movies_scores = []
    for i, movie_title in enumerate(movies_list):
        payload = {'first': 'yes', 'kp_query': movie_title}
        kinopoisk_page_html = fetch_site_page(
            proxies_list,
            KINOPOISK_PAGE_URL,
            payload
        )
        rating, reviews_amount = get_movie_score(kinopoisk_page_html)
        movie_scores = {
            'movie': movie_title,
            'rating': rating,
            'reviews_amount': reviews_amount
        }
        movies_scores.append(movie_scores)
        print('{}'.format(NUM_MOVIES_TO_DISPLAY - i))
    movies_scores.sort(key=lambda x: x['rating'], reverse=True)
    output_movies_to_console(movies_scores)
