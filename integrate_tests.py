import unittest
import osd

class IntegrateTests(unittest.TestCase):
     def value_right(user_value, value):
         if(abs(value-user_value)>3):
               return 0
         else:
               return 1

     def test_distance_right(self):
         self.assertIsTrue(value_right(user_distance, distance),  "distance accuracy should be less than 3 sm")

     def test_height(self):
          self.assertIsTrue(value_right(user_height, real_object_height),  "height accuracy should be less than 3 sm")
     
     def test_width(self):
          self.assertIsTrue(value_right(user_width, real_object_width),  "width accuracy should be less than 3 sm")

