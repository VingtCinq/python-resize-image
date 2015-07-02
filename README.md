A python package to easily resize images
========================================

This package gives function for easily resizing images.

The following functions are supported:

* `resize_cover` resize the image the fill the specified area, crop as needed (same behavior as `background-size: cover`).
* `resize_contain` resize the image to can fit in the specified area, keeping the ratio and without crop (same behavior as `background-size: contain`). 
* `resize_width` resize the image to the specified width ajusting height to keep the ratio the same.
* `resize_height` resize the image to the specified height ajusting width to keep the ratio the same.
* `resize_crop` crop the image with a centered rectangle of the specified size.



Installation
------------

Install python-resize-image by running:

```
pip install python-resize-image
```


Usage
-----

```python
from PIL import Image
from cStringIO import StringIO

from imageresize import imageresize


with Image.open('test-image.jpeg') as image:
    cover = imageresize.resize_cover(image, [200, 100])
    cover.save('test-image-cover.jpeg', image.format)
```

Tests
----------

```
pip install -r requirements.dev.txt
pip install -e .
python setup.py test
```


Contribute
----------

python-resize-image is hosted at [github.com/VingtCinq/python-resize-image/](https://github.com/VingtCinq/python-resize-image).


Support
-------

If you are having issues, please let us know.


License
-------

The project is licensed under the MIT License.
