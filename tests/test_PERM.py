import algorithms.PERM as algo
import unittest
import os

script_dir = os.path.dirname(__file__)  # absolute dir the script is in


class TestAlgo(unittest.TestCase):

    def test_PERM_1(self):
        """

        Rosalind Test
        :return:
        """
        sample_answer = [6, [1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
        rel_path = "../datasets/PERM_1.txt"
        abs_file_path = os.path.join(script_dir, rel_path)
        result = algo.main_PERM(abs_file_path)
        self.assertEqual(sample_answer, result)

    def test_PERM_2(self):
        """

        Test for invalid input
        :return:
        """
        rel_path = "../datasets/LCSQ_2.txt"
        abs_file_path = os.path.join(script_dir, rel_path)
        with self.assertRaises(ValueError):
            algo.main_PERM(abs_file_path)

    def test_PERM_3(self):
        """

        Test for empty input
        :return:
        """
        rel_path = "../datasets/LCSQ_3.txt"
        abs_file_path = os.path.join(script_dir, rel_path)
        with self.assertRaises(ValueError):
            algo.main_PERM(abs_file_path)




if __name__ == '__main__':
    unittest.main()  # pragma: no cover