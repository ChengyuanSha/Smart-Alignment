from algorithms.REVC import main_REVC
import unittest
import os

script_dir = os.path.dirname(__file__)  # absolute dir the script is in


class TestAlgo(unittest.TestCase):

    def test_DNA_1(self):
        sample_answer = 'ACCGGGTTTT'
        rel_path = "../datasets/REVC_1.txt"
        abs_file_path = os.path.join(script_dir, rel_path)
        result = main_REVC(abs_file_path)
        self.assertEqual(sample_answer, result)

    def test_DNA_2(self):
        sample_answer = 'ACCCAAAACGGCAGTTCCTGCTGGATTGGATTTTTTACGAAAAGCTCCACAGTGTAAGATCAA'
        rel_path = "../datasets/REVC_2.txt"
        abs_file_path = os.path.join(script_dir, rel_path)
        result = main_REVC(abs_file_path)
        self.assertEqual(sample_answer, result)

    def test_DNA_3(self):
        rel_path = "../datasets/REVC_3.txt"
        abs_file_path = os.path.join(script_dir, rel_path)
        with self.assertRaises(Exception) as context:
            main_REVC(abs_file_path)
        self.assertTrue('Input Error' in str(context.exception))


if __name__ == '__main__':
    unittest.main()  # pragma: no cover