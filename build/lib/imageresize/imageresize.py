from __future__ import division
from PIL import Image

def crop(image, size):
    img_format = image.format
    old_size = image.size
    left = int((old_size[0] - size[0])/2)
    top = int((old_size[1] - size[1])/2)
    right = int(old_size[0] - left)
    bottom = int(old_size[1] - top)
    crop = image.crop((left, top, right, bottom))
    crop.format = img_format
    return crop

def resize_cover(image, size):
    """
    Resize image according to size.
    size is a list of two values, respectively [width, height]
    """
    img_format = image.format
    img = image.copy()
    img_size = img.size
    if (img_size[0] >= size[0] and img_size[1] >= size[1]):
        ratio = max(size[0]/img_size[0], size[1]/img_size[1])
        new_size = [int(img_size[0]*ratio), int(img_size[1]*ratio)]
        img = img.resize((new_size[0],new_size[1]), Image.LANCZOS)
        img = crop(img, size)
        img.format = img_format
        return img
    else:
        raise ValueError(u"Your image is too small. Minimum size: %s" % size)

def resize_contain(image, size):
    """
    Resize image according to size.
    size is a list of two values, respectively [width, height]
    """
    img_format = image.format
    img = image.copy()
    img_size = img.size
    if (img_size[0] >= size[0] or img_size[1] >= size[1]):
        img.thumbnail((size[0], size[1]), Image.LANCZOS)
        background = Image.new('RGBA', (size[0], size[1]), (255, 255, 255, 0))
        backgroung_size = (int((size[0] - img.size[0]) / 2), int((size[1] - img.size[1]) / 2))
        background.paste(img, backgroung_size)
        background.format = img_format
        return background
    else:
        raise ValueError(u"Your image is too small. Minimum size: %s" % size)

def resize_by_width(image, width):
    """
    Resize image according to size.
    size is a list of two values, respectively [width, height]
    """
    img_format = image.format
    img = image.copy()
    img_size = img.size
    if (img_size[0] >= width):
        new_height = int((width/img_size[0])*img_size[1])
        img.thumbnail((width, new_height), Image.LANCZOS)
        img.format = img_format
        return img
    else:
        raise ValueError(u"Your image is too small. Minimum size: %s" % size)

def resize_by_height(image, height):
    """
    Resize image according to size.
    size is a list of two values, respectively [width, height]
    """
    img_format = image.format
    img = image.copy()
    img_size = img.size
    if (img_size[1] >= height):
        new_width = int((height/img_size[1])*img_size[0])
        img.thumbnail((new_width, height), Image.LANCZOS)
        img.format = img_format
        return img
    else:
        raise ValueError(u"Your image is too small. Minimum size: %s" % size)

def resize_thumbnail(image, size):
    """
    Resize image according to size.
    size is a list of two values, respectively [width, height]
    """
    img_format = image.format
    img = image.copy()
    img.thumbnail((size[0], size[1]), Image.LANCZOS)    
    img.format = img_format
    return img
