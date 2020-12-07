import unittest
from princesspeach import answer

class Testprincesspeach(unittest.TestCase):
    def test1_answer(self):
        self.assertEqual(answer(15,5,[4,9,2]), "0\n1\n3\n5\n6\n7\n8\n10\n11\n12\n13\n14\nMario got 3 of the dangerous obstacles.", "broken")

    def test2_answer(self):
        self.assertEqual(answer(10,4,[1,2,3]), "0\n4\n5\n6\n7\n8\n9\nMario got 3 of the dangerous obstacles.", "broken")
        
    def test3_answer(self):
        self.assertEqual(answer(9,6,[4,2,0,6]), "1\n3\n5\n7\n8\nMario got 4 of the dangerous obstacles.", "broken")
    
if __name__ == "__main__":
    unittest.main(verbosity=2)