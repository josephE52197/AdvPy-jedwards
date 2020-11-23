import unittest
from onechicken import answer

class Testonechicken(unittest.TestCase):
    def test1_answer(self):
        self.assertEqual(answer(55,75), "Dr. Chaz will have 20 pieces of chicken left over!", "broken")
    
    def test2_answer(self):
        self.assertEqual(answer(99,100), "Dr. Chaz will have 1 piece of chicken left over!", "broken")
    
    def test3_answer(self):
        self.assertEqual(answer(55,54), "Dr. Chaz needs 1 more piece of chicken!", "broken")


if __name__ == "__main__":
    unittest.main(verbosity=2)