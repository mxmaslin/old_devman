import re

from flask import render_template, request

from app import app


def cycle_through_text(closing_quote_pos, current_pos, text, nice_text, quote):
    tag_open = text.find('<', current_pos)
    opening_quote_pos = text.find(quote, current_pos)
    if 0 <= tag_open < opening_quote_pos:
        current_pos = text.find('>', tag_open)
    elif (tag_open >= 0 and opening_quote_pos < tag_open) or tag_open < 0:
        closing_quote_pos = text.find(quote, opening_quote_pos + 1)
        if closing_quote_pos > 0 and (tag_open < 0 or closing_quote_pos < tag_open):
            nice_text[opening_quote_pos] = '«'
            nice_text[closing_quote_pos] = '»'
            current_pos = closing_quote_pos
        else:
            current_pos = opening_quote_pos + 1
    return opening_quote_pos, closing_quote_pos, current_pos


def fix_quotes(text, quote):
    if not text:
        return ''
    nice_text = list(text)
    opening_quote_pos, closing_quote_pos = 0, 0
    current_pos = 0
    while True:
        if opening_quote_pos < 0:
            break
        opening_quote_pos, closing_quote_pos, current_pos = cycle_through_text(closing_quote_pos, current_pos, text, nice_text, quote)
    return ''.join(nice_text)


def fix_hyphens(text):
    text = text.replace(' ‐ ', ' — ')
    return text


def fix_phone_numbers(text):
    return re.sub(r'(\d)‐(\d)', r'\1–\2', text)


def fix_words_after_digits(text):
    return re.sub(r'(\d) ([a-zA-Z])', r'\1&nbsp;\2', text)


def fix_extra_space_characters(text):
    return re.sub(r'[\n\r ]{2,}', r' ', text)


def fix_conjunctions(text):
    compiled = re.compile(
        r'''((^[A-Z])|  # conjunction at the beginning of text or 
             ( [a-z])|  # conjunction in the middle of sentence or
             (\. [A-Z]) # conjunction at the beginning of second or more sentence
             ){1}       # the conjunction consists of one symbol
             \ +(\w)    # trailed by word symbol''',
        re.VERBOSE
    )
    return re.sub(compiled, r'\1&nbsp;\5', text)


def get_nice_text(text):
    nice_text = fix_quotes(text, '"')
    nice_text = fix_quotes(nice_text, '\'')
    nice_text = fix_hyphens(nice_text)
    nice_text = fix_phone_numbers(nice_text)
    nice_text = fix_words_after_digits(nice_text)
    nice_text = fix_extra_space_characters(nice_text)
    nice_text = fix_conjunctions(nice_text)
    return nice_text


@app.route('/', methods=['POST', 'GET'])
def form():
    context = dict()
    if request.method == 'POST':
        form_data = request.form
        text = form_data.get('text')
        nice_text = get_nice_text(text)
        context = {'nice_text': nice_text, 'text': text}
    return render_template('form.html', context=context)
