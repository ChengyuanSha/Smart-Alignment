from algorithms.SUBS import main_SUBS, read_input
import unittest
import os
script_dir = os.path.dirname(__file__) # absolute dir the script is in

class TestAlgo(unittest.TestCase):

    def test_SUBS_1(self):
        sample_answer = [2, 4, 10]
        rel_path = "../datasets/SUBS_1.txt"
        abs_file_path = os.path.join(script_dir, rel_path)
        seq = read_input(abs_file_path)
        result = main_SUBS(seq)
        self.assertEqual(sample_answer, result)

    def test_SUBS_2(self):
        sample_answer = [1, 7, 12]
        rel_path = "../datasets/SUBS_2.txt"
        abs_file_path = os.path.join(script_dir, rel_path)
        seq = read_input(abs_file_path)
        result = main_SUBS(seq)
        self.assertEqual(sample_answer, result)

    def test_SUBS_3(self):
        sample_answer = []
        rel_path = "../datasets/SUBS_3.txt"
        abs_file_path = os.path.join(script_dir, rel_path)
        seq = read_input(abs_file_path)
        result = main_SUBS(seq)
        self.assertEqual(sample_answer, result)

if __name__ == '__main__':
    unittest.main() # pragma: no cover