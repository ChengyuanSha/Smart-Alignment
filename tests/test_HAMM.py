from algorithms.HAMM import main_HAMM, read_input
import unittest
import os

script_dir = os.path.dirname(__file__)  # absolute dir the script is in


class TestAlgo(unittest.TestCase):

    def test_DNA_1(self):
        sample_answer = 7
        rel_path = "../datasets/HAMM_1.txt"
        abs_file_path = os.path.join(script_dir, rel_path)
        dna1, dna2 = read_input(abs_file_path)
        result = main_HAMM(dna1, dna2)
        self.assertEqual(sample_answer, result)

    def test_DNA_2(self):
        sample_answer = 515
        rel_path = "../datasets/HAMM_2.txt"
        abs_file_path = os.path.join(script_dir, rel_path)
        dna1, dna2 = read_input(abs_file_path)
        result = main_HAMM(dna1, dna2)
        self.assertEqual(sample_answer, result)

    def test_DNA_3(self):
        rel_path = "../datasets/HAMM_3.txt"
        abs_file_path = os.path.join(script_dir, rel_path)
        with self.assertRaises(Exception) as context:
            dna1, dna2 = read_input(abs_file_path)
            main_HAMM(dna1, dna2)
        self.assertTrue('Input Error' in str(context.exception))


if __name__ == '__main__':
    unittest.main()  # pragma: no cover