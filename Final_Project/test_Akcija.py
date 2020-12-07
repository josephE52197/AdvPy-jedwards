import unittest
from Akcija import answer

class TestAkcija(unittest.TestCase):
    def test1_answer(self):
        input1 = [1,4,7,4,2,7]
        self.assertEqual(answer(input1), 20, "broken")
    def test2_answer(self):
        input2 = [6,9,4,2,0]
        self.assertEqual(answer(input2), 17, "broken")
    def test3_answer(self):
        input3 = [1,3,3,7,8,0,0,8,2]
        self.assertEqual(answer(input3), 23, "broken")
    

if __name__ == "__main__":
    unittest.main(verbosity=2)