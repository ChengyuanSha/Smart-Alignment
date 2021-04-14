from algorithms.PROT import main_PROT, read_input
import unittest
import os
script_dir = os.path.dirname(__file__) # absolute dir the script is in

class TestAlgo(unittest.TestCase):

    def test_DNA_1(self):
        sample_answer = 'MAMAPRTEINSTRING'
        rel_path = "../datasets/PROT_1.txt"
        abs_file_path = os.path.join(script_dir, rel_path)
        dna = read_input(abs_file_path)
        result = main_DNA(dna)
        self.assertEqual(sample_answer, result)


if __name__ == '__main__':
    unittest.main() # pragma: no cover