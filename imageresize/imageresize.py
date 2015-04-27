from PIL import Image
import math

def crop(image, size):
	img_format = image.format
	old_size = image.size
	left = (size[0] - old_size[0])/2
	top = (size[1] - old_size[1])/2
	right = size[0] - left
	bottom = size[1] - top
	crop = image.crop((left, top, right, bottom))
	crop.format = img_format
	return crop

def resize_cover(image, size):
	"""
	Resize image according to size.
	size is a list of two values, respectively [width, height]
	"""
	img = image.copy()
	img_size = img.size
	if (img_size[0] >= size[0] and img_size[1] >= size[1]):
		img_format = img.format
		ratio = max(size[0]/float(img_size[0]), size[1]/float(img_size[1]))
		new_size = [int(math.ceil(img_size[0]*ratio)), int(math.ceil(img_size[1]*ratio))]
		img = img.resize((new_size[0],new_size[1]), Image.LANCZOS)
		img = crop(img, size, img.size)
		img.format = img_format
		return img
	else:
		raise ValueError(u"Your image is too small. Minimum size: %s" % size)

def resize_contain(image, size):
	"""
	Resize image according to size.
	size is a list of two values, respectively [width, height]
	"""
	img = image.copy()
	img_size = img.size
	if (img_size[0] >= size[0] or img_size[1] >= size[1]):
		image_format = img.format
		img.thumbnail((size[0], size[1]), Image.LANCZOS)
		background = Image.new('RGBA', (size[0], size[1]), (255, 255, 255, 0))
		img = background.paste(img, ((size[0] - img.size[0]) / 2, (size[1] - img.size[1]) / 2))
		img.format = img_format
		return img
	else:
		raise ValueError(u"Your image is too small. Minimum size: %s" % size)

def resize_by_width(image, width):
	"""
	Resize image according to size.
	size is a list of two values, respectively [width, height]
	"""
	img = image.copy()
	img_size = img.size
	if (img_size[0] >= width):
		new_height = math.ceil((width/img_size[0])*img_size[1])
		image_format = img.format
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
	img = image.copy()
	img_size = img.size
	if (img_size[1] >= height):
		new_width = math.ceil((height/img_size[1])*img_size[0])
		image_format = img.format
		img.thumbnail((height, new_width), Image.LANCZOS)
		img.format = img_format
		return img
	else:
		raise ValueError(u"Your image is too small. Minimum size: %s" % size)

def resize_thumbnail(image, size):
	"""
	Resize image according to size.
	size is a list of two values, respectively [width, height]
	"""
	image_format = img.format
	img = image.copy()
	img.thumbnail((size[0], size[1]), Image.LANCZOS)	
	img.format = img_format
	return img
