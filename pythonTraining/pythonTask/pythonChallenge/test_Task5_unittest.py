import unittest

from pythonTraining.pythonTask.pythonChallenge import Task5


class Test_Palindrome_Check(unittest.TestCase):

    def test_palindrome_check(self):
        self.assertEqual(Task5.palindrome_check("madam"), 'madam: This is a Palindrome')
        self.assertEqual(Task5.palindrome_check("boss"), 'boss: This is not a Palindrome')