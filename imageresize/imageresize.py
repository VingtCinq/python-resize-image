from __future__ import division
from PIL import Image
import imageexceptions
import math

def resize_crop(image, size):
    """
    Crop the image with a centered rectangle of the specified size
    image: a Pillow image instance
    size: a list of two integers [width, height]
    """
    img_format = image.format
    image = image.copy()
    old_size = image.size
    if old_size[0] >= size[0] and old_size[1] >= size[1]:
        left = int(math.ceil((old_size[0] - size[0])/2))
        top = int(math.ceil((old_size[1] - size[1])/2))
        right = int(math.ceil(old_size[0] - left))
        bottom = int(math.ceil(old_size[1] - top))
        crop = int(image.crop((left, top, right, bottom)))
        crop.format = img_format
        return crop
    else:
        raise imageexceptions.ImageSizeError(old_size, size)

def resize_cover(image, size):
    """
    Resize image according to size.
    image: a Pillow image instance
    size: a list of two integers [width, height]
    """
    img_format = image.format
    img = image.copy()
    img_size = img.size
    if (img_size[0] >= size[0] and img_size[1] >= size[1]):
        ratio = max(size[0]/img_size[0], size[1]/img_size[1])
        new_size = [int(math.ceil(img_size[0]*ratio)), int(math.ceil(img_size[1]*ratio))]
        img = img.resize((new_size[0],new_size[1]), Image.LANCZOS)
        img = resize_crop(img, size)
        img.format = img_format
        return img
    else:
        raise imageexceptions.ImageSizeError(img_size, size)

def resize_contain(image, size):
    """
    Resize image according to size.
    image: a Pillow image instance
    size: a list of two integers [width, height]
    """
    img_format = image.format
    img = image.copy()
    img_size = img.size
    img.thumbnail((size[0], size[1]), Image.LANCZOS)
    background = Image.new('RGBA', (size[0], size[1]), (255, 255, 255, 0))
    img_position = (int(math.ceil((size[0] - img.size[0]) / 2)), int(math.ceil((size[1] - img.size[1]) / 2)))
    background.paste(img, img_position)
    background.format = img_format
    return background

def resize_width(image, width):
    """
    Resize image according to size.
    image: a Pillow image instance
    size: a list of two integers [width, height]
    """
    img_format = image.format
    img = image.copy()
    img_size = img.size
    if (img_size[0] >= width):
        new_height = int(math.ceil((width/img_size[0])*img_size[1]))
        img.thumbnail((width, new_height), Image.LANCZOS)
        img.format = img_format
        return img
    else:
        raise imageexceptions.ImageSizeError(img_size[0], width)

def resize_height(image, height):
    """
    Resize image according to size.
    image: a Pillow image instance
    size: a list of two integers [width, height]
    """
    img_format = image.format
    img = image.copy()
    img_size = img.size
    if (img_size[1] >= height):
        new_width = int(math.ceil((height/img_size[1])*img_size[0]))
        img.thumbnail((new_width, height), Image.LANCZOS)
        img.format = img_format
        return img
    else:
        raise imageexceptions.ImageSizeError(img_size[1], height)

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
