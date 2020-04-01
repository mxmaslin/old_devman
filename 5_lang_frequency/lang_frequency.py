import re
from argparse import ArgumentParser
from collections import Counter


def get_console_args():
    parser = ArgumentParser(description='Get path to text file')
    parser.add_argument('filepath', type=str, help='Path to text file')
    parser.add_argument('top', type=int, help='Amount of top words')
    return parser.parse_args()


def load_data(filepath):
    try:
        with open(filepath) as file:
            return file.read()
    except FileNotFoundError:
        return None


def get_most_frequent_words(text, amount_of_top_words):
    try:
        text = re.findall(r'[а-яА-Яa-zA-Z]+', text)
        return Counter(text).most_common(amount_of_top_words)
    except AttributeError:
        return None


def print_most_frequent(words):
    for word, count in words:
        word_data_phrase_template = "- '{}': {} раз(а)"
        print(word_data_phrase_template.format(word, count))


if __name__ == '__main__':
    console_args = get_console_args()
    filepath = console_args.filepath
    amount_of_top_words = console_args.top
    text = load_data(filepath)
    if not text:
        exit('Извините, не удалось прочитать текст из файла')
    most_frequent_words = get_most_frequent_words(text, amount_of_top_words)
    freq_announcement = 'Частота {} самых часто встречающихся слов в файле {}:'
    print(freq_announcement.format(amount_of_top_words, filepath))
    print_most_frequent(most_frequent_words)
