from algorithms.GAFF_extension import read_fasta, BLOSUM62, GAFF_extended, main_extension

import unittest
import os

script_dir = os.path.dirname(__file__)  # absolute dir the script is in


class TestAlgo(unittest.TestCase):

    def test_DNA_1(self):
        sample_answer1 = 2
        sample_answer2 = "PRT---EINS"
        sample_answer3 = "PRTWPSEIN-"
        rel_path = '../datasets/extension_4.txt'
        abs_file_path = os.path.join(script_dir, rel_path)
        max_score, s_aligned, t_aligned  = main_extension(abs_file_path, BLOSUM62(), -11, -1)
        self.assertEqual(sample_answer1, max_score)
        self.assertEqual(sample_answer2, s_aligned)
        self.assertEqual(sample_answer3, t_aligned)

    def test_DNA_2(self):
        sample_answer1 = 2
        sample_answer2 = "AAAAAMHASYPYASTAHYAAA----AAAA----"
        sample_answer3 = "--------------TANYSTATDQM----HSTS"
        rel_path = '../datasets/extension_5.txt'
        abs_file_path = os.path.join(script_dir, rel_path)
        max_score, s_aligned, t_aligned = main_extension(abs_file_path, BLOSUM62(), -11, -1, ignore_start_gaps=True,
                       conserved_seq="A", conserved_strength=20,
                       ignore_end_gaps=True, auto_bound=True)
        self.assertEqual(sample_answer1, max_score)
        self.assertEqual(sample_answer2, s_aligned)
        self.assertEqual(sample_answer3, t_aligned)

    def test_DNA_3(self):
        rel_path = '../datasets/extension_6.txt'
        abs_file_path = os.path.join(script_dir, rel_path)
        with self.assertRaises(Exception) as context:
            s, t = read_fasta(abs_file_path)
            GAFF_extended(s, t, BLOSUM62(), -11, -1)
        self.assertTrue('Input Error' in str(context.exception))


if __name__ == '__main__':
    unittest.main()  # pragma: no cover
