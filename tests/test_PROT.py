from algorithms.PROT import main_PROT, read_input
import unittest
import os
script_dir = os.path.dirname(__file__) # absolute dir the script is in

class TestAlgo(unittest.TestCase):

    def test_PROT_1(self):
        sample_answer = 'MAMAPRTEINSTRING'
        rel_path = "../datasets/PROT_1.txt"
        abs_file_path = os.path.join(script_dir, rel_path)
        seq = read_input(abs_file_path)
        result = main_PROT(seq)
        self.assertEqual(sample_answer, result)

    def test_PROT_2(self):
        sample_answer = 'DTAESISRATRSANSISTIRSN'
        rel_path = "../datasets/PROT_2.txt"
        abs_file_path = os.path.join(script_dir, rel_path)
        seq = read_input(abs_file_path)
        result = main_PROT(seq)
        self.assertEqual(sample_answer, result)

    def test_PROT_3(self):
        sample_answer = ''
        rel_path = "../datasets/PROT_3.txt"
        abs_file_path = os.path.join(script_dir, rel_path)
        seq = read_input(abs_file_path)
        result = main_PROT(seq)
        self.assertEqual(sample_answer, result)

if __name__ == '__main__':
    unittest.main() # pragma: no cover