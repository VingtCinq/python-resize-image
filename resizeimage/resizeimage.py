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
        def wrapper(image, size, validate=True, *args, **kwargs):
            if validate:
                validator(image, size)
            return func(image, size, *args, **kwargs)
        return wrapper

    return decorator


def _is_big_enough(image, size):
    """Check that the image's size superior to `size`"""
    if (size[0] > image.size[0]) and (size[1] > image.size[1]):
        raise ImageSizeError(image.size, size)


def _width_is_big_enough(image, width):
    """Check that the image width is superior to `width`"""
    if width > image.size[0]:
        raise ImageSizeError(image.size[0], width)


def _height_is_big_enough(image, height):
    """Check that the image height is superior to `height`"""
    if height > image.size[1]:
        raise ImageSizeError(image.size[1], height)


@validate(_is_big_enough)
def resize_crop(image, size):
    """
    Crop the image with a centered rectangle of the specified size
    image:      a Pillow image instance
    size:       a list of two integers [width, height]
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
def resize_cover(image, size, resample=Image.LANCZOS):
    """
    Resize image according to size.
    image:      a Pillow image instance
    size:       a list of two integers [width, height]
    """
    img_format = image.format
    img = image.copy()
    img_size = img.size
    ratio = max(size[0] / img_size[0], size[1] / img_size[1])
    new_size = [
        int(math.ceil(img_size[0] * ratio)),
        int(math.ceil(img_size[1] * ratio))
    ]
    img = img.resize((new_size[0], new_size[1]), resample)
    img = resize_crop(img, size)
    img.format = img_format
    return img


def resize_contain(image, size, resample=Image.LANCZOS, bg_color=(255, 255, 255, 0)):
    """
    Resize image according to size.
    image:      a Pillow image instance
    size:       a list of two integers [width, height]
    """
    img_format = image.format
    img = image.copy()
    img.thumbnail((size[0], size[1]), resample)
    background = Image.new('RGBA', (size[0], size[1]), bg_color)
    img_position = (
        int(math.ceil((size[0] - img.size[0]) / 2)),
        int(math.ceil((size[1] - img.size[1]) / 2))
    )
    background.paste(img, img_position)
    background.format = img_format
    return background.convert('RGBA')


@validate(_width_is_big_enough)
def resize_width(image, size, resample=Image.LANCZOS):
    """
    Resize image according to size.
    image:      a Pillow image instance
    size:       an integer or a list or tuple of two integers [width, height]
    """
    try:
        width = size[0]
    except:
        width = size
    img_format = image.format
    img = image.copy()
    img_size = img.size
    # If the origial image has already the good width, return it
    # fix issue #16
    if img_size[0] == width:
        return image
    new_height = int(math.ceil((width / img_size[0]) * img_size[1]))
    img.thumbnail((width, new_height), resample)
    img.format = img_format
    return img


@validate(_height_is_big_enough)
def resize_height(image, size, resample=Image.LANCZOS):
    """
    Resize image according to size.
    image:      a Pillow image instance
    size:       an integer or a list or tuple of two integers [width, height]
    """
    try:
        height = size[1]
    except:
        height = size
    img_format = image.format
    img = image.copy()
    img_size = img.size
    # If the origial image has already the good height, return it
    # fix issue #16
    if img_size[1] == height:
        return image
    new_width = int(math.ceil((height / img_size[1]) * img_size[0]))
    img.thumbnail((new_width, height), resample)
    img.format = img_format
    return img


def resize_thumbnail(image, size, resample=Image.LANCZOS):
    """
    Resize image according to size.
    image:      a Pillow image instance
    size:       a list of two integers [width, height]
    """

    img_format = image.format
    img = image.copy()
    img.thumbnail((size[0], size[1]), resample)
    img.format = img_format
    return img


def resize(method, *args, **kwargs):
    """
    Helper function to access one of the resize function.
    method:     one among 'crop', 'cover', 'contain', 'width', 'height' or 'thumbnail'
    image:      a Pillow image instance
    size:       a list or tuple of two integers [width, height]
    """
    if method not in ['crop',
                      'cover',
                      'contain',
                      'width',
                      'height',
                      'thumbnail']:
        raise ValueError(u"method argument should be one of \
            'crop', 'cover', 'contain', 'width', 'height' or 'thumbnail'")
    return getattr(sys.modules[__name__], 'resize_%s' % method)(*args, **kwargs)
