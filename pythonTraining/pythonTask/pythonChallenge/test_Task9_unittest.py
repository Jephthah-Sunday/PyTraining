import unittest

from pythonTraining.pythonTask.pythonChallenge import Task9


class ConvertToUppercase(unittest.TestCase):

    def test_convert_string_uppercase(self):
        self.assertEqual(Task9.convert_string_uppercase("madam"), 'MADAM')
        self.assertEqual(Task9.convert_string_uppercase("boss"), 'BOSS')