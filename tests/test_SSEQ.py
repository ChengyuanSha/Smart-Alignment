from algorithms.SSEQ import main_SSEQ, read_fasta
import unittest
import os
script_dir = os.path.dirname(__file__) # absolute dir the script is in

class TestAlgo(unittest.TestCase):

    def test_SSEQ_1(self):
        sample_answer = ['3', '4', '5']
        rel_path = "../datasets/SSEQ_1.txt"
        abs_file_path = os.path.join(script_dir, rel_path)
        seq = read_fasta(abs_file_path)
        result = main_SSEQ(seq)
        self.assertEqual(sample_answer, result)

    def test_SSEQ_2(self):
        sample_answer = ['2', '3', '5', '14', '15', '21', '27', '30', '36', '46']

        rel_path = "../datasets/SSEQ_2.txt"
        abs_file_path = os.path.join(script_dir, rel_path)
        seq = read_fasta(abs_file_path)
        result = main_SSEQ(seq)
        self.assertEqual(sample_answer, result)

    def test_SSEQ_3(self):
        sample_answer = []
        rel_path = "../datasets/SSEQ_3.txt"
        abs_file_path = os.path.join(script_dir, rel_path)
        seq = read_fasta(abs_file_path)
        result = main_SSEQ(seq)
        self.assertEqual(sample_answer, result)

if __name__ == '__main__':
    unittest.main() # pragma: no cover