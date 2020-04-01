import os
from argparse import ArgumentParser
from PIL import Image


def get_console_args():
    parser = ArgumentParser(
        description='Path to file, desired dimensions, where to save'
    )
    parser.add_argument('--width', type=int, nargs='?', help='Desired width')
    parser.add_argument('--height', type=int, nargs='?', help='Desired height')
    parser.add_argument('--scale', type=float, nargs='?', help='Desired scale')
    parser.add_argument(
        'original_path', type=str, help='Original file path'
    )
    parser.add_argument(
        'result_path',
        type=str, nargs='?',
        help='Path to resulting file',
        default=os.getcwd()
    )
    return parser.parse_args()


def get_original_img(file_path):
    try:
        return Image.open(file_path)
    except OSError:
        return None


def get_desired_dimensions(image, desired_width, desired_height, desired_scale):
    original_width, original_height = image.size
    if desired_scale:
        result_width = original_width * desired_scale
        result_height = original_height * desired_scale
    elif desired_width and desired_height:
        result_width = desired_width
        result_height = desired_height
    elif desired_width:
        result_width = desired_width
        result_height = result_width * (original_height / original_width)
    else:
        result_height = desired_height or original_height
        result_width = result_height * (original_width / original_height)
    return int(result_width), int(result_height)


def are_proportions_violated(image, desired_width, desired_height):
    original_proportions = int(image.width / image.height)
    result_proportions = int(desired_width / desired_height)
    return original_proportions == result_proportions


def get_result_img_name(
        img_name, desired_dimenstions, dot_extension, result_path
):
    desired_width, desired_height = desired_dimenstions
    result_img_path = os.path.join(result_path, img_name)
    result_image_name = '{}__{}x{}{}'.format(
        result_img_path, desired_width, desired_height, dot_extension
    )
    return result_image_name


def save_result_img(image, result_image_name, extension):
    try:
        image.save(result_image_name, extension)
        return True
    except FileNotFoundError:
        return False


if __name__ == '__main__':
    args = get_console_args()
    width = args.width
    height = args.height
    scale = args.scale
    original_path = args.original_path
    result_path = args.result_path

    if scale and (width or height):
        exit("Сan't use both dimension(s) and scale")

    img = get_original_img(original_path)
    if not img:
        exit("Can't find original file or wrong file format")

    if width and height and are_proportions_violated(img, width, height):
        print('Proportions warning: image will be stretched')

    desired_dimenstions = get_desired_dimensions(img, width, height, scale)
    result_img = img.resize(desired_dimenstions, Image.ANTIALIAS)
    img_name, dot_extension = os.path.splitext(original_path)
    dot, plain_extension = dot_extension.split('.')
    result_img_name = get_result_img_name(
        img_name, desired_dimenstions, dot_extension, result_path
    )
    if not save_result_img(result_img, result_img_name, plain_extension):
        exit('{} directory does not exist'.format(result_path))
