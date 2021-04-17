from algorithms.GCON import main_GCON, read_fasta, BLOSUM62

import unittest
import os

script_dir = os.path.dirname(__file__)  # absolute dir the script is in


class TestAlgo(unittest.TestCase):

    def test_DNA_1(self):
        sample_answer = 13
        rel_path = "../datasets/GCON_1.txt"
        abs_file_path = os.path.join(script_dir, rel_path)
        s, t = read_fasta(abs_file_path)
        result = main_GCON(s, t, BLOSUM62(), -5)
        self.assertEqual(sample_answer, result)

    def test_DNA_2(self):
        sample_answer = 608
        rel_path = "../datasets/GCON_2.txt"
        abs_file_path = os.path.join(script_dir, rel_path)
        s, t = read_fasta(abs_file_path)
        result = main_GCON(s, t, BLOSUM62(), -5)
        self.assertEqual(sample_answer, result)

    def test_DNA_3(self):
        rel_path = "../datasets/GCON_3.txt"
        abs_file_path = os.path.join(script_dir, rel_path)
        with self.assertRaises(Exception) as context:
            s, t = read_fasta(abs_file_path)
            main_GCON(s, t, BLOSUM62(), -5)
        self.assertTrue('Input Error' in str(context.exception))


if __name__ == '__main__':
    unittest.main()  # pragma: no cover
