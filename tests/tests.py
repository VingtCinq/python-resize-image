import os
import shutil
import unittest
from contextlib import contextmanager

from PIL import Image

from resizeimage import resizeimage
from resizeimage.imageexceptions import ImageSizeError


class TestValidateDecorator(unittest.TestCase):

    def validation(x, y):
        if x < y:
            raise Exception()
        else:
            return True

    @staticmethod
    @resizeimage.validate(validation)
    def func(x, y):
        return x * y

    def test_no_exception(self):
        """
        Test that when the validate function does not raise an
        error, the correct result is returned.
        """
        self.assertEqual(self.func(42, 2), 84)

    def test_exception(self):
        """
        Test that when the validate fails, the exception is
        properly propagated.
        """
        with self.assertRaises(Exception):
            self.func(2, 42)

    def test_no_validation(self):
        """
        Test that when the validate fails, the exception is
        properly propagated.
        """
        self.assertEqual(self.func(2, 42, validate=False), 84)

    def test_validation_only_no_exception(self):
        """
        Test that when the validate is called directly it returns
        `True`
        """
        def validate(x):
            if x < 0:
                raise Exception()
            else:
                return True


class TestResizeimage(unittest.TestCase):
    """
    Run tests for all functions
    the given image for testing is 800x533
    """

    @classmethod
    def setUpClass(self):
        """
        Setup a temporary directory to store image
        """
        path = os.path.dirname(__file__)
        self.test_image_filepath = os.path.join(path, "test-image.jpeg")
        tmpname = 'tmp-images'
        self._tmp_dir = os.path.join(path, tmpname)
        if os.path.isdir(self._tmp_dir):
            shutil.rmtree(self._tmp_dir)
        os.makedirs(self._tmp_dir)

    def _tmp_filename(self, filename):
        """
        Get relative path for the given filename
        """
        return os.path.join(self._tmp_dir, filename)

    @contextmanager
    def _open_test_image(self):
        with open(self.test_image_filepath, 'r+b') as f:
            image = Image.open(f)
            yield image

    def test_resize_crop(self):
        """
        Test that the image resized with resize_crop
        has the expected size
        """
        with self._open_test_image() as img:
            img = resizeimage.resize_crop(img, [200, 200])
            filename = self._tmp_filename('crop.jpeg')
            img.save(filename, img.format)
            with Image.open(filename) as image:
                self.assertEqual(image.size, (200, 200))

    def test_can_not_resize_crop_larger_size(self):
        """
        Test that resizing an image with resize_crop
        to a size larger than the original raises an error
        """
        with self._open_test_image() as img:
            with self.assertRaises(ImageSizeError):
                resizeimage.resize_crop(img, (801, 534))

    def test_resize_cover(self):
        """
        Test that the image resized with resize_cover
        has the expected size
        """
        with self._open_test_image() as img:
            img = resizeimage.resize_cover(img, [200, 100])
            filename = self._tmp_filename('resize-cover.jpeg')
            img.save(filename, img.format)
            with Image.open(filename) as image:
                self.assertEqual(image.size, (200, 100))

    def test_can_not_resize_cover_larger_size(self):
        """
        Test that resizing an image with resize_cover
        to a size larger than the original raises an error
        """
        with self._open_test_image() as img:
            with self.assertRaises(ImageSizeError):
                resizeimage.resize_cover(img, (801, 534))

    def test_resize_contain(self):
        """
        Test that the image resized with resize_contain
        has the expected size
        """
        with self._open_test_image() as img:
            img = resizeimage.resize_contain(img, [200, 100])
            filename = self._tmp_filename('resize-contain.jpeg')
            img.save(filename, img.format)
            with Image.open(filename) as image:
                self.assertEqual(image.size, (200, 100))

    def test_resize_contain_larger_size(self):
        """
        Test that the image resized with resize_contain
        has the expected size
        """
        with self._open_test_image() as img:
            img = resizeimage.resize_contain(img, [801, 534])
            filename = self._tmp_filename('resize-contain-larger.jpeg')
            img.save(filename, img.format)
            with Image.open(filename) as image:
                self.assertEqual(image.size, (801, 534))

    def test_resize_width(self):
        """
        Test that the image resized with resize_width
        has the expected size
        """
        with self._open_test_image() as img:
            img = resizeimage.resize_width(img, 200)
            filename = self._tmp_filename('resize-width.jpeg')
            img.save(filename, img.format)
            with Image.open(filename) as image:
                self.assertEqual(image.size[0], 200)

    def test_can_not_resize_larger_width(self):
        """
        Test that resizing an image with resize_width
        to a size larger than the original raises an error
        """
        with self._open_test_image() as img:
            with self.assertRaises(ImageSizeError):
                resizeimage.resize_width(img, 801)

    def test_resize_height(self):
        """
        Test that the image resized with resize_height
        has the expected size
        """
        with self._open_test_image() as img:
            img = resizeimage.resize_height(img, 200)
            filename = self._tmp_filename('resize-height.jpeg')
            img.save(filename, img.format)
            with Image.open(filename) as image:
                self.assertEqual(image.size[1], 200)

    def test_can_not_resize_larger_height(self):
        with self._open_test_image() as img:
            with self.assertRaises(ImageSizeError):
                resizeimage.resize_height(img, 534)

    def test_resize_thumbnail(self):
        """
        Test that the image resized with resize_thumbnail
        has the expected size
        """
        with self._open_test_image() as img:
            img = resizeimage.resize_thumbnail(img, [200, 200])
            filename = self._tmp_filename('resize-thumbnail.jpeg')
            img.save(filename, img.format)
            with Image.open(filename) as image:
                self.assertEqual(image.size, (200, 133))


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestResizeimage)
    unittest.TextTestRunner(verbosity=2).run(suite)
