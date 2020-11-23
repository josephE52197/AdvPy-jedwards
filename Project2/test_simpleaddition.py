import unittest
from simpleaddition import answer

class Testsimpleaddition(unittest.TestCase):
    def test1_answer(self):
        self.assertEqual(answer(69,420), 489, "broken")
    
    def test2_answer(self):
        self.assertEqual(answer(234,1123), 1357, "broken")
    
    def test3_answer(self):
        self.assertEqual(answer(5311,11111111), 11116422, "broken")


if __name__ == "__main__":
    unittest.main(verbosity=2)