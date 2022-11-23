import unittest

from pythonTraining.pythonTask.pythonChallenge import Challenge10


class ConvertToUppercase(unittest.TestCase):

    def test_convert_string_sentencecase(self):
        self.assertEqual(Challenge10.convert_string_sentencecase("madam"), 'Madam')
        self.assertEqual(Challenge10.convert_string_sentencecase("boss"), 'Boss')