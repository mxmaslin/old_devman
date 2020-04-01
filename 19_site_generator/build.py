import json
import os
import re

import markdown2

from jinja2 import Environment, FileSystemLoader


def get_file_content(filepath):
    with open(filepath) as file:
        return file.read()


def save_to_file(content, filepath):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, 'w+') as file:
        file.write(content)


def extract_int(fname_string):
    match = re.search(r'\d+', fname_string)
    if match:
        return int(match.group(0))
    return float('inf')


def get_index_context(config):
    index_context = config['topics']
    for topic in index_context:
        files = [x for x in config['articles'] if x['topic'] == topic['slug']]
        files.sort(key=lambda x: extract_int(x['source'].split('/')[1]))
        topic['files'] = files
    return index_context


def create_html_page(md_file):
    path_to_md = md_file['source']
    full_path_to_md = os.path.join('articles', path_to_md)
    md_file_content = get_file_content(full_path_to_md)
    html = markdown2.markdown(md_file_content)
    article_content = article_template.render(article=html)
    path_to_html = path_to_md.replace('.md', '.html')
    save_to_file(
        article_content, os.path.join('rendered', path_to_html)
    )


if __name__ == '__main__':
    articles_folder = 'articles'
    config_file = get_file_content('config.json')
    config = json.loads(config_file)
    index_context = get_index_context(config)

    env = Environment(loader=FileSystemLoader('templates'))

    index_template = env.get_template('index.html')
    index_content = index_template.render(context=index_context)
    save_to_file(index_content, os.path.join('rendered', 'index.html'))

    article_template = env.get_template('article.html')

    for section in index_context:
        for md_file in section['files']:
            create_html_page(md_file)
