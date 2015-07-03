# A python package to easily resize images


This package provides function for easily resizing images.

The following functions are supported:

* `resize_crop` crop the image with a centered rectangle of the specified size.
* `resize_cover` resize the image the fill the specified area, crop as needed (same behavior as `background-size: cover`).
* `resize_contain` resize the image to can fit in the specified area, keeping the ratio and without crop (same behavior as `background-size: contain`). 
* `resize_height` resize the image to the specified height ajusting width to keep the ratio the same.
* `resize_width` resize the image to the specified width ajusting height to keep the ratio the same.
* `resize_thumbnail` resize image while keeping the ratio trying its best to match the specified size.



## Installation


Install python-resize-image using pip:

```
pip install python-resize-image
```


## Usage


python-resize-image takes as first argument a `PIL.Image` and then `size` argument which can be a single integer or tuple of two integers.

In the following example, we open an image, crop it and save as new file:

```python
from PIL import Image

from resizeimage import resizeimage


with Image.open('test-image.jpeg') as image:
    cover = resizeimage.resize_cover(image, [200, 100])
    cover.save('test-image-cover.jpeg', image.format)
```

Before resizing, python-image-resize will check wether the operation can be done. A resize is considered valid if it doesn't require to increase
one of the dimension. To avoid the test add `validate=False` as argument:

```python
cover = resizeimage.resize_cover(image, [200, 100], validate=False)
```

You can also create a two step process validation then processing using `validate` function attached to resized function which allows to test the viability of the resize without doing it just after validation. `validate` is available using the dot `.` operator on every resize function e.g. `resize_cover.validate`.

The first exemple is rewritten in the following snippet to use this feature:

```python
from PIL import Image

from resizeimage import resizeimage


with Image.open('test-image.jpeg') as image:
    is_valid = resizeimage.resize_cover.validate(image, [200, 100])

# do something else...

if is_valid:
    with Image.open('test-image.jpeg') as image:
        resizeimage.resize_cover.validate(image, [200, 100], validate=False)
        cover = resizeimage.resize_cover(image, [200, 100]) 
        cover.save('test-image-cover.jpeg', image.format)
```

Mind the fact that it's useless to validate the image twice, so we pass `validate=False` to `resize_cover.validate`.

## API Reference

### `resize_crop(image, size, validate=True)`

Crop the image with a centered rectangle of the specified size.

Crop an image with a 200x200 cented square:

```python
from PIL import Image

test_img = open('test-image.jpeg', 'rw')
img = Image.open(test_img)
img = resizeimage.resize_crop(img, [200, 200])
img.save('test-image-crop.jpeg', img.format)
```

### `resize_cover(image, size, validate=True)`

Resize the image the fill the specified area, crop as needed. It's the same behavior as css `background-size: cover` property.

Resize and crop (from center) the image so that it covers a 200x100 rectangle.

```python
from PIL import Image

test_img = open('test-image.jpeg', 'rw')
img = Image.open(test_img)
img = resizeimage.resize_cover(img, [200, 100])
img.save('test-image-cover.jpeg', img.format)
```

### `resize_contain(image, size, validate=True)`

Resize the image to can fit in the specified area, keeping the ratio and without crop. It's the same behavior as css `background-size: contain` property. A white a background border is created.

Resize the image to minimum so that it is contained in a 200x100 rectangle is the ratio between source and destination image.

```python
from PIL import Image

test_img = open('test-image.jpeg', 'rw')
img = Image.open(test_img)
img = resizeimage.resize_contain(img, [200, 100])
img.save('test-image-contain.jpeg', img.format)
```

### `resize_height(image, width, validate=True)`

Resize the image to the specified height ajusting width to keep the ratio the same.

Resize the image to be 200px width:

```python
from PIL import Image

test_img = open('test-image.jpeg', 'rw')
img = Image.open(test_img)
img = resizeimage.resize_width(img, 200)
img.save('test-image-width.jpeg', img.format)
```

### `resize_height(image, height, validate=True)`

Resize the image to the specified width ajusting height to keep the ratio the same.

Resize the image to be 200px height:

```python
from PIL import Image

test_img = open('test-image.jpeg', 'rw')
img = Image.open(test_img)
img = resizeimage.resize_height(img, 200)
img.save('test-image-height.jpeg', img.format)
```

### `resize_thumbnail(image, size, validate=True)`

Resize image while keeping the ratio trying its best to match the specified size.

Resize the image to be contained in a 200px square:

```python
from PIL import Image

test_img = open('test-image.jpeg', 'rw')
img = Image.open(test_img)
img = resizeimage.resize_thumbnail(img, [200, 200])
img.save('test-image-thumbnail.jpeg', img.format)
```

## Tests

```
pip install -r requirements.dev.txt
pip install -e .
python setup.py test
```

## Contribute

python-resize-image is hosted at [github.com/VingtCinq/python-resize-image/](https://github.com/VingtCinq/python-resize-image).


## Support

If you are having issues, please let us know.

## License

The project is licensed under the MIT License.
