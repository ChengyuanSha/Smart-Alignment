from algorithms.SPLC import main_SPLC, read_fasta
import unittest
import os
script_dir = os.path.dirname(__file__) # absolute dir the script is in

class TestAlgo(unittest.TestCase):

    def test_SPLC_1(self):
        sample_answer = 'MVYIADKQHVASREAYGHMFKVCA'
        rel_path = "../datasets/SPLC_1.txt"
        abs_file_path = os.path.join(script_dir, rel_path)
        input = read_fasta(abs_file_path)
        result = main_SPLC(input)
        self.assertEqual(sample_answer, result)


if __name__ == '__main__':
    unittest.main() # pragma: no cover