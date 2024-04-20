import unittest
from up_low import up_low


class TestUpLow(unittest.TestCase):

    def test_all_uppercase(self):
        result = up_low('HELLO')
        self.assertEqual(result, {'upper': 5, 'lower': 0})

    def test_all_lowercase(self):
        result = up_low('hello')
        self.assertEqual(result, {'upper': 0, 'lower': 5})

    def test_mixed_case(self):
        result = up_low('Hello World')
        self.assertEqual(result, {'upper': 2, 'lower': 8})

    def test_empty_string(self):
        result = up_low('')
        self.assertEqual(result, {'upper': 0, 'lower': 0})

    def test_special_characters(self):
        result = up_low('!@#$%^&*()')
        self.assertEqual(result, {'upper': 0, 'lower': 0})


if __name__ == '__main__':
    unittest.main()
