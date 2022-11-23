import unittest

from pythonTraining.pythonTask.pythonChallenge import Challenge9


class ConvertToUppercase(unittest.TestCase):

    def test_convert_string_uppercase(self):
        self.assertEqual(Challenge9.convert_string_uppercase("madam"), 'MADAM')
        self.assertEqual(Challenge9.convert_string_uppercase("boss"), 'BOSS')