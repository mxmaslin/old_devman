import json
import math
from argparse import ArgumentParser


def get_console_args():
    parser = ArgumentParser()
    parser.add_argument('-lat', '--lat', help='latitude', type=float)
    parser.add_argument('-lon', '--lon', help='longitude', type=float)
    parser.add_argument('filepath', help='path to json', type=str)
    return parser.parse_args()


def get_bars_file(filepath):
    try:
        with open(filepath) as file:
            return file.read()
    except FileNotFoundError:
        return None


def get_bars_data(bars_file):
    try:
        bars_json = json.loads(bars_file)
        return bars_json['features']
    except json.decoder.JSONDecodeError:
        return None


def get_bar_by_size(bars, chooser):
    try:
        return chooser(
            bars,
            key=lambda x: x['properties']['Attributes']['SeatsCount']
        )
    except KeyError:
        return None


def get_distance(bar, lon, lat):
    bar_lon = bar['geometry']['coordinates'][0]
    bar_lat = bar['geometry']['coordinates'][1]
    return math.hypot(lon - bar_lon, lat - bar_lat)


def get_closest_bar(bars, lon, lat):
    try:
        return min(bars, key=lambda x: get_distance(x, lon, lat))
    except (TypeError, IndexError):
        return None


def get_bar_description(bar, criteria):
    error = "{} bar information wasn't found".format(criteria)
    try:
        bar_name = bar['properties']['Attributes']['Name']
        seats_num = bar['properties']['Attributes']['SeatsCount']
        address = bar['properties']['Attributes']['Address']
        description = '{} bar is: {}. It has {} seats. Its location is {}'
        return description.format(criteria, bar_name, seats_num, address)
    except (KeyError, TypeError):
        return error


if __name__ == '__main__':
    console_args = get_console_args()
    filepath = console_args.filepath
    bars_file = get_bars_file(filepath)
    if not bars_file:
        exit("Sorry, file wasn't found")
    bars_data = get_bars_data(bars_file)
    if not bars_data:
        exit('Sorry, file content is invalid')
    largest = get_bar_by_size(bars_data, max)
    print(get_bar_description(largest, 'Largest'))
    smallest = get_bar_by_size(bars_data, min)
    print(get_bar_description(smallest, 'Smallest'))
    lon = console_args.lon
    lat = console_args.lat
    closest = get_closest_bar(bars_data, lon, lat)
    print(get_bar_description(closest, 'Closest'))
