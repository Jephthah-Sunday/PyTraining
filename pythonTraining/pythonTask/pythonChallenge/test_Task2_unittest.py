import unittest

from pythonTraining.pythonTask.pythonChallenge import Task2


class TestPowerofNumber(unittest.TestCase):

    def test_powerOfNumber(self):
        self.assertEqual(Task2.powerOfNumber(4, 2), 16)



if __name__ == '__main__':
    unittest.main()