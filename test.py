from fractions import Fraction

import unittest

from my_sum import sum


class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)

    def test_list_fraction(self):
        """
        Test that it can sum a list of fractions
        """
        data = [Fraction(1, 4), Fraction(1, 4), Fraction(2, 5)]
        result = sum(data)
        self.assertEqual(result, 1)

if __name__ == "__main_":
    unittest.main()

    #the tests that I tried at the beginning worked fine as expected. Each of the tested sumsvalues were equal to the expected sum. Meaning if the values tested were 1,2,3,4 the expected value was 10
    #for this fraction test, the test result was Fraction(9,10) !=1 meaning that the tested fraction was not equal to the expected value.