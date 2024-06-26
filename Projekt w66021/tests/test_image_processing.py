

import unittest
from PIL import Image

from image_processing import resize_image

class TestImageProcessing(unittest.TestCase):

    def test_resize_image(self):
    
        image_path = 'test_image.jpg' 
        new_width = 200
        new_height = 150

     
        resized_image = resize_image(image_path, new_width, new_height)

        
        self.assertEqual(resized_image.size, (new_width, new_height))

if __name__ == '__main__':
    unittest.main()
