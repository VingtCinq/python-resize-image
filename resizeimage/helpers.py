import requests
from cStringIO import StringIO
from PIL import Image


def file_to_image(image_file_name):
    """
    Convert a file into a Pillow Image object
    """
    with open(image_file_name, 'r') as f_image:
        return Image.open(f_image)


def url_to_image(url):
    """
    Fetch an image from url and convert it into a Pillow Image object
    """
    r = requests.get(url)
    image = StringIO(r.content)
    return image


def string_to_image(image_string):
    """
    Convert string datas into a Pillow Image object
    """
    image_filelike = StringIO(image_string)
    image = Image.open(image_filelike)
    return image
