A python package to easily resize images
========================================

This package gives function for easily resizing images.

The following functions are supported :

1. resize_cover 
2. resize_contain 
3. resize_by_width 
4. resize_by_height 
5. crop 


Here is a full example :

```python
from imageresize import imageresize
from cStringIO import StringIO
from PIL import Image

test_img = open('test-image.jpeg', 'rw')

img = Image.open(test_img)
img = imageresize.crop(img, [200, 200])
img.save('test-image-crop.jpeg', img.format)


img = Image.open(test_img)
img = imageresize.resize_cover(img, [200, 100])
img.save('test-image-cover.jpeg', img.format)


img = Image.open(test_img)
img = imageresize.resize_contain(img, [200, 100])
img.save('test-image-contain.jpeg', img.format)


img = Image.open(test_img)
img = imageresize.resize_by_width(img, 200)
img.save('test-image-width.jpeg', img.format)


img = Image.open(test_img)
img = imageresize.resize_by_height(img, 200)
img.save('test-image-height.jpeg', img.format)


img = Image.open(test_img)
img = imageresize.resize_thumbnail(img, [200, 200])
img.save('test-image-thumbnail.jpeg', img.format)
```