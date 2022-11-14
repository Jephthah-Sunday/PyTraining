import unittest

from unit_testing.unittestTrainingLog import bodmas


class TestBodmas(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(bodmas.addition(3, 1), 4)
        self.assertEqual(bodmas.addition(3, 7), 10)
        self.assertEqual(bodmas.addition(3, 5), 8)

    def test_subtraction(self):
        self.assertEqual(bodmas.subtraction(3, 2), 1)
        self.assertEqual(bodmas.subtraction(9, 3), 6)


if __name__ == '__main__':
    unittest.main()

