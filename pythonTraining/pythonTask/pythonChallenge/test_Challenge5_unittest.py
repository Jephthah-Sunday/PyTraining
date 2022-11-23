import unittest

from pythonTraining.pythonTask.pythonChallenge import Challenge5


class Test_Palindrome_Check(unittest.TestCase):

    def test_palindrome_check(self):
        self.assertEqual(Challenge5.palindrome_check("madam"), 'madam: This is a Palindrome')
        self.assertEqual(Challenge5.palindrome_check("boss"), 'boss: This is not a Palindrome')