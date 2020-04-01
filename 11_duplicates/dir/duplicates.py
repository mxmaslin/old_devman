import os
from argparse import ArgumentParser


def get_console_args():
    parser = ArgumentParser(description='Input path to directory')
    parser.add_argument('dirpath', type=str, help='Path to directory')
    return parser.parse_args()


def find_duplicates(dir_tree):
    for dir, subdirs, files in dir_tree:
        print(dir, subdirs, files)


def print_duplicates(duplicates):
    pass


if __name__ == '__main__':
    args = get_console_args()
    dir_path = args.dirpath
    dir_tree = os.walk(dir_path)
    # duplicates = find_duplicates(dir_tree)
    find_duplicates(dir_tree)
    # print_duplicates(duplicates)





