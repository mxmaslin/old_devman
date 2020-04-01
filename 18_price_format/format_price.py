from argparse import ArgumentParser


def get_console_args():
    parser = ArgumentParser(description='Get formatting options')
    parser.add_argument('price', type=float)
    return parser.parse_args()


def format_price(price):
    if isinstance(price, bool):
        return None
    try:
        price = float(price)
    except (ValueError, TypeError):
        return None

    if round(price, 2).is_integer():
        return '{:,.0f}'.format(price).replace(',', ' ')
    return '{:,.2f}'.format(price).replace(',', ' ')


if __name__ == '__main__':
    args = get_console_args()
    price = args.price
    formatted_price = format_price(price)
    print(formatted_price)
