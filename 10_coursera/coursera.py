import json
import requests
from argparse import ArgumentParser
from bs4 import BeautifulSoup
from lxml import html
from openpyxl import Workbook


def get_console_args():
    parser = ArgumentParser(description='Get amount of Coursera courses')
    parser.add_argument(
        'courses_amount',
        type=int,
        nargs='?',
        default=20,
        help='Amount of courses'
    )
    parser.add_argument(
        'resulting_xls_filepath',
        default='result.xls',
        help='Path to resulting xls file'
    )
    return parser.parse_args()


def get_page_response_content(courses_list_url):
    response = requests.get(courses_list_url)
    return response.content


def get_courses_urls(page_response_content, courses_amount):
    tree = html.fromstring(page_response_content)
    courses_urls = tree.xpath('//loc/text()')
    return courses_urls[:courses_amount]


def get_course_name(parsed_page):
    h1_placement_index = 1
    return parsed_page.find_all('h1')[h1_placement_index].get_text()


def get_course_languages(parsed_page):
    course_languages_container_class_name = 'ProductGlance'
    last_child_index = -1
    course_languages = parsed_page.find(
        'div',
        {'class': course_languages_container_class_name}
    ).find_all('h4')[last_child_index].get_text()
    return course_languages


def get_course_start_date(parsed_page):
    ajax_text = parsed_page.find(
        'script', type='application/ld+json'
    ).get_text()
    try:
        start_date = json.loads(
            ajax_text)['@graph'][1]['hasCourseInstance']['startDate']
    except(TypeError, KeyError):
        return None
    return start_date


def get_course_num_weeks(parsed_page):
    course_num_weeks = len(parsed_page.find_all(
        'div',
        {'class': 'SyllabusWeek'}
    ))
    return course_num_weeks


def get_course_rating(parsed_page):
    try:
        course_rating = parsed_page.find(
            'div',
            {'class': 'CourseRating'}
        ).find('span').get_text()
    except AttributeError:
        return None
    return course_rating


def get_course_metadata(parsed_course_page):
    course_name = get_course_name(parsed_course_page)
    course_languages = get_course_languages(parsed_course_page)
    course_start_date = get_course_start_date(parsed_course_page)
    course_num_weeks = get_course_num_weeks(parsed_course_page)
    course_rating = get_course_rating(parsed_course_page)
    return (course_name,
            course_languages,
            course_start_date,
            course_num_weeks,
            course_rating
            )


if __name__ == '__main__':
    args = get_console_args()
    courses_amount = args.courses_amount
    resulting_xls_filepath = args.resulting_xls_filepath
    courses_list_url = 'https://www.coursera.org/sitemap~www~courses.xml'
    page_response_content = get_page_response_content(courses_list_url)
    courses_urls = get_courses_urls(page_response_content, courses_amount)
    workbook = Workbook()
    worksheet = workbook.active
    for course_url in courses_urls:
        course_page = get_page_response_content(course_url)
        parsed_course_page = BeautifulSoup(course_page, 'html.parser')
        course_metadata = get_course_metadata(parsed_course_page)
        worksheet.append(course_metadata)
    workbook.save(resulting_xls_filepath)
