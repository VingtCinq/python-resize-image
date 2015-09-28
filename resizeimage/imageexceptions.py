

class ImageSizeError(Exception):
    """
    Raised when the supplied image does not
    fit the intial size requirements
    """
    def __init__(self, actual_size, required_size):
        self.message = 'Image is too small, Image size : %s, Required size : %s' % (actual_size, required_size)
        self.actual_size = actual_size
        self.required_size = required_size

    def __str__(self):
        return repr(self.message)
