import unittest
from eulersnumber import answer

class Testeulersnumber(unittest.TestCase):
    def test1_answer(self):
        self.assertEqual(answer(2), 2.5, "broken")
    def test2_answer(self):
        self.assertEqual(answer(5), 2.7166666666666663, "broken")
    def test3_answer(self):
        self.assertEqual(answer(300), 2.7182818284590455, "broken")
    
if __name__ == "__main__":
    unittest.main(verbosity=2)