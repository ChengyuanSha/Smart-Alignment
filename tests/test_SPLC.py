from algorithms.SPLC import main_SPLC, read_fasta
import unittest
import os
script_dir = os.path.dirname(__file__) # absolute dir the script is in

class TestAlgo(unittest.TestCase):

    def test_SPLC_1(self):
        sample_answer = 'MVYIADKQHVASREAYGHMFKVCA'
        rel_path = "../datasets/SPLC_1.txt"
        abs_file_path = os.path.join(script_dir, rel_path)
        seq = read_fasta(abs_file_path)
        result = main_SPLC(seq)
        self.assertEqual(sample_answer, result)

    def test_SPLC_2(self):
        sample_answer = 'FTGVFVTLTEL'
        rel_path = "../datasets/SPLC_2.txt"
        abs_file_path = os.path.join(script_dir, rel_path)
        seq = read_fasta(abs_file_path)
        result = main_SPLC(seq)
        self.assertEqual(sample_answer, result)

    def test_SPLC_3(self):
        rel_path = "../datasets/SPLC_3.txt"
        abs_file_path = os.path.join(script_dir, rel_path)
        with self.assertRaises(Exception) as context:
            seq = read_fasta(abs_file_path)
            main_SPLC(seq)
        self.assertTrue('No exons detected.' in str(context.exception))

if __name__ == '__main__':
    unittest.main() # pragma: no cover