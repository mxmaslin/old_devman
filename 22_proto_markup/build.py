from collections import OrderedDict
from staticjinja import Site


def generate_placeholder_content(content_item, items_amount):
    return [content_item for _ in range(items_amount)]


if __name__=='__main__':
    bid = {
        "date": "вчера, в 21:30",
        "content": "60 шт. ПК от 75-15 до ПК 21-15, Криводановка, с доставкой.",
        "bidder": "Алексей",
        "phone": "8-999-888-77-66",
        "views": 12
    }
    bids_amount = 10
    bids = generate_placeholder_content(bid, bids_amount)
    region = 'Новосибирск и область'
    user_name = 'Леонид Федорович'
    context = {'bids': bids, 'region': region, 'user_name': user_name}
    context_part = dict(context)
    context_part['bids'] = bids[:4]
    review = {
        "author": "Кирилл, 29 лет, г.Барабинск",
        "content": "Бла-бла, мне помогло. Бла-бла, всё супер!" * 4
    }
    reviews_amount = 3
    context_part['reviews'] = generate_placeholder_content(
        review, reviews_amount
    )
    site = Site.make_site(
        contexts=[
            ('index.html', context_part),
            ('zajavki.html', context)
        ],
        outpath='rendered',
        staticpaths=['assets/css', 'assets/img', 'assets/js']

    )
    site.render(use_reloader=True)
