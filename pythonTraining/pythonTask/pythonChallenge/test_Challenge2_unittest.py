import unittest

from pythonTraining.pythonTask.pythonChallenge import Challenge2


class TestPowerofNumber(unittest.TestCase):

    def test_powerOfNumber(self):
        self.assertEqual(Challenge2.powerOfNumber(4, 2), 16)



if __name__ == '__main__':
    unittest.main()