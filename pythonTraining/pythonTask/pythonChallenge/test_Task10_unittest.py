import unittest

from pythonTraining.pythonTask.pythonChallenge import Task10


class ConvertToUppercase(unittest.TestCase):

    def test_convert_string_sentencecase(self):
        self.assertEqual(Task10.convert_string_sentencecase("madam"), 'Madam')
        self.assertEqual(Task10.convert_string_sentencecase("boss"), 'Boss')