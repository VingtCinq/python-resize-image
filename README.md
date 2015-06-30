

A python package to easily resize images
========================================

This package gives function for easily resizing images.

The following functions are supported :

* resize_cover 
* resize_contain 
* resize_width 
* resize_height 
* resize_crop 


Installation
------------

Install python-image-resize by running:

```
pip install python-image-resize
```


Usage
-----

Here is a full example :

```python
from imageresize import imageresize
from cStringIO import StringIO
from PIL import Image

test_img = open('test-image.jpeg', 'rw')

# Crop an image with a 200x200 cented square
img = Image.open(test_img)
img = imageresize.resize_crop(img, [200, 200])
img.save('test-image-crop.jpeg', img.format)


# Resize and crop (from center) the image so that it covers a 200x100 rectangle
# Same behavior as css background-size: cover property
img = Image.open(test_img)
img = imageresize.resize_cover(img, [200, 100])
img.save('test-image-cover.jpeg', img.format)


# Resize the image to minimum so that it is contained in a 200x100 rectangle
# is the ratio between source and destination image, a background border is created
# Same behavior as css background-size: contain property
img = Image.open(test_img)
img = imageresize.resize_contain(img, [200, 100])
img.save('test-image-contain.jpeg', img.format)


# Resize the image to be 200px width
img = Image.open(test_img)
img = imageresize.resize_width(img, 200)
img.save('test-image-width.jpeg', img.format)


# Resize the image to be 200px height
img = Image.open(test_img)
img = imageresize.resize_height(img, 200)
img.save('test-image-height.jpeg', img.format)


# Resize the image to be contained in a 200px square
img = Image.open(test_img)
img = imageresize.resize_thumbnail(img, [200, 200])
img.save('test-image-thumbnail.jpeg', img.format)
```

Tests
----------

```
pip install -r requirements.dev.txt
pip install -e .
make check
```


Contribute
----------

- Issue Tracker: github.com/charlesthk/python-resize-image/issues
- Source Code: github.com/charlesthk/python-resize-image


Support
-------

If you are having issues, please let us know.


License
-------

The project is licensed under the MIT License.
