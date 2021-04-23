from algorithms.EDTA import main_EDTA, read_fasta
import unittest
import os
script_dir = os.path.dirname(__file__) # absolute dir the script is in

class TestAlgo(unittest.TestCase):

    def test_EDTA_1(self):
        sample_answer = (4, 'nPRETTY--', 'PR-TTEIN')
        rel_path = "../datasets/EDTA_1.txt"
        abs_file_path = os.path.join(script_dir, rel_path)
        strings = read_fasta(abs_file_path)
        result = main_EDTA(strings)
        self.assertEqual(sample_answer, result)
        
    def test_EDTA_2(self):
        sample_answer = (28, 'A-ACC--GC-GT--CTCTACGACCGGTGCTCGATTTAAT-TTCGCCGACGT-GATGAC', 'ATTCCAGGCAGTGCCTCTGCCGCCGG-GC-CCCTCTCGTGATTG--G--GTAGTTG--')
        rel_path = "../datasets/EDTA_2.txt"
        abs_file_path = os.path.join(script_dir, rel_path)
        strings = read_fasta(abs_file_path)
        result = main_EDTA(strings)
        self.assertEqual(sample_answer, result)

    def test_EDTA_2(self):
        sample_answer = (35, 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA', 'TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT')
        rel_path = "../datasets/EDTA_2.txt"
        abs_file_path = os.path.join(script_dir, rel_path)
        strings = read_fasta(abs_file_path)
        result = main_EDTA(strings)
        self.assertEqual(sample_answer, result)

if __name__ == '__main__':
    unittest.main() # pragma: no cover