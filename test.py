import unittest
import osd

class UnitTests(unittest.TestCase):

    def test_img(self):
         self.assertEqual(img, vis, "images should be equal after copying"

    def distance_is_positive(distance):
        if (distance>0):
            return 1
        else:
            return 0

    def test_distance_is_positive(self):
        self.assertIsTrue(distance_is_positive(distance),  "distance should be over 0")

    def test_distance_not_null(self):
        self.assertIsNot(distance(), 0, "distance shouldn't be 0")

    def test_distance_not_none(self):
        self.assertIsNotNone(distance(),"distance shouldn't be none")

    def GPIO_is_one_zero(GPIO.input(GPIO_ECHO)):
        if (GPIO.input(GPIO_ECHO)==0 or GPIO.input(GPIO_ECHO)==1):
            return 1
        else:
            return 0

    def test_GPIO_is_one_zero(self):
        self.assertTrue(GPIO_is_one_zero(GPIO.input(GPIO_ECHO)), "it can be only 1 or 0")

    def test_GPIO_not_none(self):
        self.assertIsNotNone(GPIO.input(GPIO_ECHO), "it can be only 1 or 0")
    
    def test_GPIO_is_one(self):
        self.assertTrue(GPIO.input(GPIO_ECHO), "it can be only 1")

    def test_GPIO_is_zero(self):
        self.assertFalse(GPIO.input(GPIO_ECHO), "it can be only 0")

    def test_camera_capture_is_not_none(self):
        self.assertIsNotNone(camera.capture('test_image.png'),"capture is not none")

    def test_width(self):
        self.assertEqual(sum(width,extLeft[0]),extRight[0], "width=extRight[0]-extLeft[0]")
   
    def test_height(self):
        self.assertEqual(sum(height,extBot[1]),extRight[0], "height=extBot[1]-extTop[1]")

    
if __name__ == "__main__":
unittest.main()
    print("Everything passed")