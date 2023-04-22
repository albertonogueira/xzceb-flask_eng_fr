"""Translator module unit tests """

import unittest
from translator import english_to_french, french_to_english

class TestEn2Fr(unittest.TestCase):
    """Testing class En 2 Fr"""
    def test1(self):
        """ Test a non-null input """
        self.assertEqual(english_to_french('Hello'), 'Bonjour')

    def test2(self):
        """ Test a null input """
        with self.assertRaises(TypeError):
            english_to_french(None)

class TestFr2En(unittest.TestCase):
    """Testing class Fr 2 En"""
    def test1(self):
        """ Test a non-null input """
        self.assertEqual(french_to_english('Bonjour'), 'Hello')

    def test2(self):
        """ Test a null input """
        with self.assertRaises(TypeError):
            french_to_english(None)

if __name__ == '__main__':
    unittest.main()
