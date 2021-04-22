from algorithms.GLOB import main_GLOB
import unittest
import os

script_dir = os.path.dirname(__file__)  # absolute dir the script is in


class TestAlgo(unittest.TestCase):

    def test_GLOB_1(self):
        """
        Rosalind Test
        :return:
        """
        sample_answer = 8.0
        rel_path = "../datasets/GLOB_1.txt"
        abs_file_path = os.path.join(script_dir, rel_path)
        result = main_GLOB(abs_file_path)
        self.assertEqual(sample_answer, result)

    def test_GLOB_2(self):
        """
        Invalid amino acid shorthand
        :return:
        """
        rel_path = "../datasets/GLOB_2.txt"
        abs_file_path = os.path.join(script_dir, rel_path)
        with self.assertRaises(KeyError) as context:
            result = main_GLOB(abs_file_path)

    def test_GLOB_3(self):
        """
        Invalid FASTA file
        :return:
        """
        rel_path = "../datasets/GLOB_3.txt"
        abs_file_path = os.path.join(script_dir, rel_path)
        with self.assertRaises(IndexError) as context:
            result = main_GLOB(abs_file_path)

    def test_GLOB_4(self):
        """
        Empty .txt File
        :return:
        """
        rel_path = "../datasets/GLOB_4.txt"
        abs_file_path = os.path.join(script_dir, rel_path)
        with self.assertRaises(IndexError) as context:
            result = main_GLOB(abs_file_path)


if __name__ == '__main__':
    unittest.main()  # pragma: no cover