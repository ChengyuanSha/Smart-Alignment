import algorithms.EDIT as algo
import unittest
import os

script_dir = os.path.dirname(__file__)  # absolute dir the script is in


class TestAlgo(unittest.TestCase):

    def test_EDIT_1(self):
        """
        Rosalind Test
        :return:
        """
        sample_answer = 5
        rel_path = "../datasets/EDIT_1.txt"
        abs_file_path = os.path.join(script_dir, rel_path)
        result = algo.main_EDIT(abs_file_path)
        self.assertEqual(sample_answer, result)

    def test_EDIT_2(self):
        """
        Invalid FASTA file
        :return:
        """
        rel_path = "../datasets/EDIT_2.txt"
        abs_file_path = os.path.join(script_dir, rel_path)
        with self.assertRaises(IndexError) as context:
            result = algo.main_EDIT(abs_file_path)

    def test_EDIT_3(self):
        """
        Empty .txt File
        :return:
        """
        rel_path = "../datasets/EDIT_3.txt"
        abs_file_path = os.path.join(script_dir, rel_path)
        with self.assertRaises(IndexError) as context:
            result = algo.main_EDIT(abs_file_path)




if __name__ == '__main__':
    unittest.main()  # pragma: no cover