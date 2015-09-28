"""main module with resize and validation functions"""
from __future__ import division
import math
import sys
from functools import wraps

from PIL import Image
from .imageexceptions import ImageSizeError


def validate(validator):
    """
    Return a decorator that validates arguments with provided `validator`
    function.

    This will also store the validator function as `func.validate`.
    The decorator returned by this function, can bypass the validator
    if `validate=False` is passed as argument otherwise the fucntion is
    called directly.

    The validator must raise an exception, if the function can not
    be called.
    """

    def decorator(func):
        """Bound decorator to a particular validator function"""

        @wraps(func)
        def wrapper(image, size, validate=True):
            if validate:
                validator(image, size)
            return func(image, size)
        return wrapper

    return decorator


def _is_big_enough(image, size):
    """Check that the image's size superior to `size`"""
    if (size[0] > image.size[0]) and (size[1] > image.size[1]):
        raise ImageSizeError(image.size, size)


def _width_is_big_enough(image, size):
    """Check that the image width is superior to `size`"""
    if size >= image.size[0]:
        raise ImageSizeError(image.size[0], size)


def _height_is_big_enough(image, size):
    """Check that the image height is superior to `size`"""
    if size >= image.size[1]:
        raise ImageSizeError(image.size[1], size)


@validate(_is_big_enough)
def resize_crop(image, size):
    """
    Crop the image with a centered rectangle of the specified size
    image: a Pillow image instance
    size: a list of two integers [width, height]
    """
    img_format = image.format
    image = image.copy()
    old_size = image.size
    left = (old_size[0] - size[0]) / 2
    top = (old_size[1] - size[1]) / 2
    right = old_size[0] - left
    bottom = old_size[1] - top
    rect = [int(math.ceil(x)) for x in (left, top, right, bottom)]
    left, top, right, bottom = rect
    crop = image.crop((left, top, right, bottom))
    crop.format = img_format
    return crop


@validate(_is_big_enough)
def resize_cover(image, size):
    """
    Resize image according to size.
    image: a Pillow image instance
    size: a list of two integers [width, height]
    """
    img_format = image.format
    img = image.copy()
    img_size = img.size
    ratio = max(size[0] / img_size[0], size[1] / img_size[1])
    new_size = [
        int(math.ceil(img_size[0] * ratio)),
        int(math.ceil(img_size[1] * ratio))
    ]
    img = img.resize((new_size[0], new_size[1]), Image.LANCZOS)
    img = resize_crop(img, size)
    img.format = img_format
    return img


def resize_contain(image, size):
    """
    Resize image according to size.
    image: a Pillow image instance
    size: a list of two integers [width, height]
    """
    img_format = image.format
    img = image.copy()
    img.thumbnail((size[0], size[1]), Image.LANCZOS)
    background = Image.new('RGBA', (size[0], size[1]), (255, 255, 255, 0))
    img_position = (
        int(math.ceil((size[0] - img.size[0]) / 2)),
        int(math.ceil((size[1] - img.size[1]) / 2))
    )
    background.paste(img, img_position)
    background.format = img_format
    return background


@validate(_width_is_big_enough)
def resize_width(image, width):
    """
    Resize image according to size.
    image: a Pillow image instance
    size: a list of two integers [width, height]
    """
    img_format = image.format
    img = image.copy()
    img_size = img.size
    new_height = int(math.ceil((width / img_size[0]) * img_size[1]))
    img.thumbnail((width, new_height), Image.LANCZOS)
    img.format = img_format
    return img


@validate(_height_is_big_enough)
def resize_height(image, height):
    """
    Resize image according to size.
    image: a Pillow image instance
    size: a list of two integers [width, height]
    """
    img_format = image.format
    img = image.copy()
    img_size = img.size
    new_width = int(math.ceil((height / img_size[1]) * img_size[0]))
    img.thumbnail((new_width, height), Image.LANCZOS)
    img.format = img_format
    return img


def resize_thumbnail(image, size):
    """
    Resize image according to size.
    image: a Pillow image instance
    size: a list of two integers [width, height]
    """
    img_format = image.format
    img = image.copy()
    img.thumbnail((size[0], size[1]), Image.LANCZOS)
    img.format = img_format
    return img


def resize(method, image, size):
    """
    Helper function to access one of the resize function.
    image: a Pillow image instance
    """
    if method not in ['crop',
                      'cover',
                      'contain',
                      'width',
                      'height',
                      'thumbnail']:
        method = 'thumbnail'
    return getattr(sys.modules[__name__], 'resize_%s' % method)(image, size)


def resize_from_file(method, image_file_name_in, size, image_file_name_out=None):
    """
    Helper function to access one of the resize function.
    If an image_file_name_out is specified, the image is saved inside
    """
    with open(image_file_name_in, 'r') as fd_image_in:
        image_in = Image.open(fd_image_in)
        out_image = resize(method, image_in, size)
        if image_file_name_out is not None:
            out_image.save(image_file_name_out, out_image.format)
            out_image.close()
        return out_image