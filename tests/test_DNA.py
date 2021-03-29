from algorithms.DNA import main_DNA, read_input
import unittest


class TestAlgo(unittest.TestCase):

    def test_DNA_1(self):
        sample_answer = '20 12 17 21'
        result = main_DNA(read_input('../datasets/DNA_1.txt'))
        self.assertEqual(sample_answer, result)

    def test_DNA_2(self):
        sample_answer = '238 189 235 251'
        result = main_DNA(read_input('../datasets/DNA_2.txt'))
        self.assertEqual(sample_answer, result)

    def test_DNA_3(self):
        with self.assertRaises(Exception) as context:
            main_DNA(read_input('../datasets/DNA_3.txt'))
        self.assertTrue('Input Error' in str(context.exception))


if __name__ == '__main__':
    unittest.main()
