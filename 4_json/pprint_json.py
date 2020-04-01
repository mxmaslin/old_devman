import json
from argparse import ArgumentParser


def get_command_line_args():
    parser = ArgumentParser()
    parser.add_argument('filepath', help='path to json', type=str)
    return parser.parse_args()


def get_file_content(filepath):
    try:
        with open(filepath, encoding='utf8') as file:
            return file.read()
    except FileNotFoundError:
        return None


def get_parsed_json(file_content):
    try:
        return json.loads(file_content)
    except json.decoder.JSONDecodeError:
        return None


def print_pretty_json(dict_from_file):
    print(json.dumps(
        dict_from_file, ensure_ascii=False, indent=4, sort_keys=True)
    )


if __name__ == '__main__':
    args = get_command_line_args()
    filepath = args.filepath
    file_content = get_file_content(filepath)
    if not file_content:
        exit("Sorry, file {} does not exist".format(filepath))
    parsed_json = get_parsed_json(file_content)
    if not parsed_json:
        exit("Sorry, file {} does not contain valid json".format(filepath))
    print_pretty_json(parsed_json)
