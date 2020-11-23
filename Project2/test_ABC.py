import unittest
from ABC import answer

class TestABC(unittest.TestCase):
    def test1_answer(self):
        input1 = [8,3,1]
        alph1 = "ABC"
        self.assertEqual(answer(input1,alph1), "1 3 8", "broken")
    def test2_answer(self):
        input2 = [4,2,5]
        alph2 = "BCA"
        self.assertEqual(answer(input2,alph2), "4 5 2", "broken")
    def test3_answer(self):
        input3 = [9,2,7]
        alph3 = "ACB"
        self.assertEqual(answer(input3,alph3), "2 9 7", "broken")
    

if __name__ == "__main__":
    unittest.main(verbosity=2)
