import unittest

import task26


class Testcompare_strings(unittest.TestCase):

    def test_compareStrings(self):
        self.assertEqual(task26.compareStrings("boy", "boy"), print('These are similar'))
        self.assertEqual(task26.compareStrings("boy", "girl"), print('These are not similar'))


    def test_compareNumbers(self):
        self.assertEqual(task26.compareNumbers(104, 389), print('These are different numbers'))

        self.assertEqual(task26.compareNumbers(456, 456), print('These are not different numbers'))




if __name__ == '__main__':
    unittest.main()