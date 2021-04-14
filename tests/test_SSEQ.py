from algorithms.SSEQ import main_SSEQ, read_fasta
import unittest
import os
script_dir = os.path.dirname(__file__) # absolute dir the script is in

class TestAlgo(unittest.TestCase):

    def test_SSEQ_1(self):
        sample_answer = '3 8 10'
        rel_path = "../datasets/SSEQ_1.txt"
        abs_file_path = os.path.join(script_dir, rel_path)
        input = read_fasta(abs_file_path)
        result = main_SSEQ(input)
        self.assertEqual(sample_answer, result)


if __name__ == '__main__':
    unittest.main() # pragma: no cover