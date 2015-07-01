import os
import unittest
import shutil

from PIL import Image

from imageresize import imageresize
from imageresize.imageexceptions import ImageSizeError


class TestImageResize(unittest.TestCase):
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

    def test_resize_crop(self):
        """
        Test that the image resized with resize_crop
        has the expected size
        """
        with Image.open(self.test_image_filepath) as img:
            img = imageresize.resize_crop(img, [200, 200])
            filename = self._tmp_filename('crop.jpeg')
            img.save(filename, img.format)
            with Image.open(filename) as image:
                self.assertEqual(image.size, (200, 200))

    def test_can_not_resize_crop_larger_size(self):
        """
        Test that resizing an image with resize_crop
        to a size larger than the original raises an error
        """
        with Image.open(self.test_image_filepath) as img:
            with self.assertRaises(ImageSizeError):
                imageresize.resize_crop(img, (801, 534))

    def test_resize_cover(self):
        """
        Test that the image resized with resize_cover
        has the expected size
        """
        with Image.open(self.test_image_filepath) as img:
            img = imageresize.resize_cover(img, [200, 100])
            filename = self._tmp_filename('resize-cover.jpeg')
            img.save(filename, img.format)
            with Image.open(filename) as image:
                self.assertEqual(image.size, (200, 100))

    def test_can_not_resize_cover_larger_size(self):
        """
        Test that resizing an image with resize_cover
        to a size larger than the original raises an error
        """
        with Image.open(self.test_image_filepath) as img:
            with self.assertRaises(ImageSizeError):
                imageresize.resize_cover(img, (801, 534))

    def test_resize_contain(self):
        """
        Test that the image resized with resize_contain
        has the expected size
        """
        with Image.open(self.test_image_filepath) as img:
            img = imageresize.resize_contain(img, [200, 100])
            filename = self._tmp_filename('resize-contain.jpeg')
            img.save(filename, img.format)
            with Image.open(filename) as image:
                self.assertEqual(image.size, (200, 100))

    def test_resize_contain_larger_size(self):
        """
        Test that the image resized with resize_contain
        has the expected size
        """
        with Image.open(self.test_image_filepath) as img:
            img = imageresize.resize_contain(img, [801, 534])
            filename = self._tmp_filename('resize-contain-larger.jpeg')
            img.save(filename, img.format)
            with Image.open(filename) as image:
                self.assertEqual(image.size, (801, 534))

    def test_resize_width(self):
        """
        Test that the image resized with resize_width
        has the expected size
        """
        with Image.open(self.test_image_filepath) as img:
            img = imageresize.resize_width(img, 200)
            filename = self._tmp_filename('resize-width.jpeg')
            img.save(filename, img.format)
            with Image.open(filename) as image:
                self.assertEqual(image.size[0], 200)

    def test_can_not_resize_larger_width(self):
        """
        Test that resizing an image with resize_width
        to a size larger than the original raises an error
        """
        with Image.open(self.test_image_filepath) as img:
            with self.assertRaises(ImageSizeError):
                imageresize.resize_width(img, 801)

    def test_resize_height(self):
        """
        Test that the image resized with resize_height
        has the expected size
        """
        with Image.open(self.test_image_filepath) as img:
            img = imageresize.resize_height(img, 200)
            filename = self._tmp_filename('resize-height.jpeg')
            img.save(filename, img.format)
            with Image.open(filename) as image:
                self.assertEqual(image.size[1], 200)

    def test_can_not_resize_larger_height(self):
        with Image.open(self.test_image_filepath) as img:
            with self.assertRaises(ImageSizeError):
                imageresize.resize_height(img, 534)

    def test_resize_thumbnail(self):
        """
        Test that the image resized with resize_thumbnail
        has the expected size
        """
        with Image.open(self.test_image_filepath) as img:
            img = imageresize.resize_thumbnail(img, [200, 200])
            filename = self._tmp_filename('resize-thumbnail.jpeg')
            img.save(filename, img.format)
            with Image.open(filename) as image:
                self.assertEqual(image.size, (200, 133))


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestImageResize)
    unittest.TextTestRunner(verbosity=2).run(suite)
