from cStringIO import StringIO
from PIL import Image
from imageresize import imageresize
from imageresize.imageexceptions import ImageSizeError

test_img = open('test-image.jpeg', 'rw')

img = Image.open(test_img)
try:
	img = imageresize.crop(img, [2000, 2000])
except ImageSizeError as e:
	print e.message
else:
	img.save('test-image-crop.jpeg', img.format)


img = Image.open(test_img)
try:
	img = imageresize.resize_cover(img, [200, 100])
except ImageSizeError as e:
	print e.message
else:
	img.save('test-image-cover.jpeg', img.format)


img = Image.open(test_img)
img = imageresize.resize_contain(img, [200, 100])
img.save('test-image-contain.jpeg', img.format)


img = Image.open(test_img)
try:
	img = imageresize.resize_by_width(img, 200)
except ImageSizeError as e:
	print e.message
else:
	img.save('test-image-width.jpeg', img.format)


img = Image.open(test_img)
try:
	img = imageresize.resize_by_height(img, 200)
except ImageSizeError as e:
	print e.message
else:
	img.save('test-image-height.jpeg', img.format)


img = Image.open(test_img)
img = imageresize.resize_thumbnail(img, [200, 200])
img.save('test-image-thumbnail.jpeg', img.format)