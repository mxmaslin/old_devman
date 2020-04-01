import getpass
import re
import string
from argparse import ArgumentParser


def get_command_line_args():
    parser = ArgumentParser(description='Get blacklist file path')
    parser.add_argument('fpath', type=str, help='Path to blacklist file')
    return parser.parse_args()


def load_blacklist(blacklist_file_path):
    with open(blacklist_file_path) as file:
        return file.read().splitlines()


def is_mixed_case_present(password):
    upper_case_presence = any([c.isupper() for c in password])
    lower_case_presence = any([c.islower() for c in password])
    return all([upper_case_presence, lower_case_presence])


def is_digit_and_letter_present(password):
    found_digit = bool(re.search(r'\d', password))
    found_letter = bool(re.search(r'[a-zA-Z]+', password))
    return found_digit and found_letter


def is_special_char_present(password):
    return any(
        (char in password) for char in string.punctuation
    ) and len(password) > 1


def has_good_length(password):
    good_length = 6
    return len(password) >= good_length


def get_password_strength(password, blacklist):
    too_weak_password = 1
    good_password = 10
    if password in blacklist:
        return too_weak_password
    includes_mixed_case = is_mixed_case_present(password)
    includes_letter_and_digit = is_digit_and_letter_present(password)
    includes_special_char = is_special_char_present(password)
    length_ok = has_good_length(password)
    if all([
        includes_mixed_case,
        includes_letter_and_digit,
        includes_special_char,
        length_ok
    ]):
        return good_password
    check_weight = 3
    checks = [includes_mixed_case,
              includes_letter_and_digit,
              includes_special_char,
              length_ok
              ]
    password_strength = sum(checks) * check_weight
    return password_strength if password_strength else 1


if __name__ == '__main__':
    args = get_command_line_args()
    blacklist_file_path = args.fpath
    try:
        blacklist = load_blacklist(blacklist_file_path)
    except FileNotFoundError:
        blacklist = []
        print("Blacklist file not found. Will continue without it")
    password = getpass.getpass('Please enter password: ')
    if not password:
        exit("Password can't be empty")
    password_strength = get_password_strength(password, blacklist)
    print('Password strength: {}'.format(password_strength))
