from algorithms.EDTA import main_EDTA, read_fasta
import unittest
import os
script_dir = os.path.dirname(__file__) # absolute dir the script is in

class TestAlgo(unittest.TestCase):

    def test_EDTA_1(self):
        sample_answer = (4, 'PRETTY--', 'PR-TTEIN')
        rel_path = "../datasets/EDTA_1.txt"
        abs_file_path = os.path.join(script_dir, rel_path)
        strings = read_fasta(abs_file_path)
        result = main_EDTA(strings)
        self.assertEqual(sample_answer, result)

    def test_EDTA_2(self):
        sample_answer = (28, 'AA-CC-G-C-GT-C-TCTAC-GACCGGTGCTCGAT-T--TAATTTCGCCGACGTGATGAC', 'ATTCCAGGCAGTGCCTCTGCCG-CCGG-GCCCC-TCTCGTGATTGGG--TA-GT--TG--')
        rel_path = "../datasets/EDTA_2.txt"
        abs_file_path = os.path.join(script_dir, rel_path)
        strings = read_fasta(abs_file_path)
        result = main_EDTA(strings)
        self.assertEqual(sample_answer, result)

    def test_EDTA_3(self):
        sample_answer = (35, 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA', 'TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT')
        rel_path = "../datasets/EDTA_2.txt"
        abs_file_path = os.path.join(script_dir, rel_path)
        strings = read_fasta(abs_file_path)
        result = main_EDTA(strings)
        self.assertEqual(sample_answer, result)

if __name__ == '__main__':
    unittest.main() # pragma: no cover