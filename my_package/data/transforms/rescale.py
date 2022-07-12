#Imports


class RescaleImage(object):
    '''
        Rescales the image to a given size.
    '''

    def __init__(self, output_size):
        '''
            Arguments:
            output_size (tuple or int): Desired output size. If tuple, output is
            matched to output_size. If int, smaller of image edges is matched
            to output_size keeping aspect ratio the same.
        '''

        # Write your code here
        self.output_size = output_size

    def __call__(self, image):
        '''
            Arguments:
            image (numpy array or PIL image)

            Returns:
            image (numpy array or PIL image)

            Note: You do not need to resize the bounding boxes. ONLY RESIZE THE IMAGE.
        '''

        if isinstance(self.output_size, tuple):
            return image.resize(self.output_size)
        else:
            w, h = image.size
            if w < h:
                return image.resize((self.output_size, int((self.output_size * h) / w)))
            else:
                return image.resize((int((self.output_size * w) / h), self.output_size))
        # Write your code here