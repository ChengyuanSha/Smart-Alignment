from algorithms.LCSM import main_LCSM
import unittest
import os

script_dir = os.path.dirname(__file__)  # absolute dir the script is in


class TestAlgo(unittest.TestCase):

    def test_LCSM_1(self):
        """
        Rosalind Test: Note the rosalind test inputs can return TA or AC
        :return:
        """
        sample_answer = 'TA'
        rel_path = "../datasets/LCSM_1.txt"
        abs_file_path = os.path.join(script_dir, rel_path)
        result = main_LCSM(abs_file_path)
        self.assertEqual(sample_answer, result)

    def test_LCSM_2(self):
        """
        Tests for invalid input from text file
        :return:
        """
        rel_path = "../datasets/LCSM_2.txt"
        abs_file_path = os.path.join(script_dir, rel_path)
        with self.assertRaises(ValueError) as context:
            result = main_LCSM(abs_file_path)

    def test_LCSM_3(self):
        """
        tests for a blank text file
        :return:
        """
        rel_path = "../datasets/LCSM_3.txt"
        abs_file_path = os.path.join(script_dir, rel_path)
        with self.assertRaises(ValueError) as context:
            result = main_LCSM(abs_file_path)

    def test_LCSM_4(self):
        """
        Tests for returning an empty substring
        :return:
        """
        sample_answer = ''
        rel_path = "../datasets/LCSM_4.txt"
        abs_file_path = os.path.join(script_dir, rel_path)
        result = main_LCSM(abs_file_path)
        self.assertEqual(sample_answer, result)

    def test_LCSM_5(self):
        """
        Tests for invalid FASTA file format
        :return:
        """
        rel_path = "../datasets/LCSM_5.txt"
        abs_file_path = os.path.join(script_dir, rel_path)
        with self.assertRaises(IndexError) as context:
            result = main_LCSM(abs_file_path)


if __name__ == '__main__':
    unittest.main()  # pragma: no cover