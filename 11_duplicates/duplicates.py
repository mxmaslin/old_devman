import os
from argparse import ArgumentParser
from collections import defaultdict


def get_console_args():
    parser = ArgumentParser(description='Input path to directory')
    parser.add_argument('dirpath', type=str, help='Path to directory')
    return parser.parse_args()


def get_files_data(dir_tree):
    files_data = defaultdict(list)
    for directory_name, subdirectory_names, file_names in dir_tree:
        for file_name in file_names:
            file_path = os.path.join(directory_name, file_name)
            file_size = os.path.getsize(file_path)
            files_data[(file_name, file_size)].append(file_path)
    return files_data


def print_duplicates_info(files_data):
    duplicates_found = False
    for (file_name, file_size), file_paths in files_data.items():
        duplicates_amount = len(file_paths)
        if duplicates_amount > 1:
            duplicates_found = True
            duples_num_message = '{} has {} duplicate(s). Their locations are:'
            print(duples_num_message.format(file_name, duplicates_amount))
            duples_location_message = '\n'.join(
                ['\t{}'.format(location) for location in file_paths]
            )
            print(duples_location_message)
    if not duplicates_found:
        print('No duplicates found')


if __name__ == '__main__':
    args = get_console_args()
    dir_path = args.dirpath
    if not os.path.isdir(dir_path):
        exit('{} is not a directory'.format(dir_path))
    dir_tree = os.walk(dir_path)
    files_data = get_files_data(dir_tree)
    print_duplicates_info(files_data)
