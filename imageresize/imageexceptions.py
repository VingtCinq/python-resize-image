

class ImageSizeError(Exception):
    """
    Raised when the supplied image does not
    fit the intial size requirements
    """
    def __init__(self, input_size, required_size):
        self.message = 'Image is too small, Image size : %s, Required size : %s' % (input_size, required_size)
        self.input_size = input_size
        self.required_size = required_size
        
    def __str__(self):
        return repr(self.message)