import os
from unittest import TestCase
from time import time

from PIL import Image, ImageOps

from imageresize import imageresize
from imageresize.imageexceptions import ImageSizeError


def abspath(filename):
    path = os.path.dirname(__file__)
    abspath = os.path.join(path, filename)
    return abspath

TEST_IMAGE_FILEPATH = abspath("test-image.jpeg")


class TestImageResize(TestCase):

    @classmethod
    def setUpClass(self):
        # setup temporary directory to store image
        # make it somewhat unique
        path = os.path.dirname(__file__)
        tmpname = str(int(time()))
        tmpname = 'tmp-images-' + tmpname
        self._tmp_dir = os.path.join(path, tmpname)
        os.makedirs(self._tmp_dir)

    def _tmp_filename(self, filename):
            return os.path.join(self._tmp_dir, filename)

    def test_resize_crop(self):
        img = Image.open(TEST_IMAGE_FILEPATH)
        img = imageresize.resize_crop(img, [200, 200])
        filename = self._tmp_filename('crop.jpeg')
        img.save(filename, img.format)
        self.assertEqual(Image.open(filename).size, (200, 200))

    def test_can_not_resize_crop_bigger_size(self):
        img = Image.open(TEST_IMAGE_FILEPATH)
        with self.assertRaises(ImageSizeError):
            imageresize.resize_crop(img, (801, 534))

    def test_resize_cover(self):
        img = Image.open(TEST_IMAGE_FILEPATH)
        img = imageresize.resize_cover(img, [200, 100])
        filename = self._tmp_filename('resize-cover.jpeg')
        img.save(filename, img.format)
        self.assertEqual(Image.open(filename).size, (200, 100))

    def test_can_not_resize_cover_bigger_size(self):
        img = Image.open(TEST_IMAGE_FILEPATH)
        with self.assertRaises(ImageSizeError):
            imageresize.resize_cover(img, (801, 534))

    def test_resize_contain(self):
        img = Image.open(TEST_IMAGE_FILEPATH)
        img = imageresize.resize_contain(img, [200, 100])
        filename = self._tmp_filename('resize-contain.jpeg')
        img.save(filename, img.format)
        self.assertEqual(Image.open(filename).size, (200, 100))

    def test_resize_width(self):
        img = Image.open(TEST_IMAGE_FILEPATH)
        img = imageresize.resize_width(img, 200)
        filename = self._tmp_filename('resize-width.jpeg')
        img.save(filename, img.format)
        self.assertEqual(Image.open(filename).size[0], 200)

    def test_can_not_resize_larger_width(self):
        img = Image.open(TEST_IMAGE_FILEPATH)
        with self.assertRaises(ImageSizeError):
            imageresize.resize_width(img, 801)

    def test_resize_height(self):
        img = Image.open(TEST_IMAGE_FILEPATH)
        img = imageresize.resize_height(img, 200)
        filename = self._tmp_filename('resize-height.jpeg')
        img.save(filename, img.format)
        self.assertEqual(Image.open(filename).size[1], 200)

    def test_can_not_resize_larger_height(self):
        img = Image.open(TEST_IMAGE_FILEPATH)
        with self.assertRaises(ImageSizeError):
            imageresize.resize_height(img, 534)

    def test_resize_thumbnail(self):
        img = Image.open(TEST_IMAGE_FILEPATH)
        img = imageresize.resize_thumbnail(img, [200, 200])
        filename = self._tmp_filename('resize-thumbnail.jpeg')
        img.save(filename, img.format)
        self.assertEqual(Image.open(filename).size, (200, 133))



if __name__ == '__main__':
    from unittest import main
    main(verbosity=2)