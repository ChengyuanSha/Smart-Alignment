import algorithms.LCSQ as algo
import unittest
import os

script_dir = os.path.dirname(__file__)  # absolute dir the script is in


class TestAlgo(unittest.TestCase):

    def test_LCSQ_1(self):
        """
        Rosalind Test
        :return:
        """
        sample_answer = 'AACTTG'
        rel_path = "../datasets/LCSQ_1.txt"
        abs_file_path = os.path.join(script_dir, rel_path)
        result = algo.main_LCSQ(abs_file_path)
        self.assertEqual(sample_answer, result)

    def test_LCSQ_2(self):
        """
        Test for invalid input
        :return:
        """
        rel_path = "../datasets/LCSQ_2.txt"
        abs_file_path = os.path.join(script_dir, rel_path)
        with self.assertRaises(IndexError) :
            algo.main_LCSQ(abs_file_path)

    def test_LCSQ_3(self):
        """
        Test for empty input
        :return:
        """
        rel_path = "../datasets/LCSQ_3.txt"
        abs_file_path = os.path.join(script_dir, rel_path)
        with self.assertRaises(IndexError):
            algo.main_LCSQ(abs_file_path)




if __name__ == '__main__':
    unittest.main()  # pragma: no cover