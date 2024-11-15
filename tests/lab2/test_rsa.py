import unittest

from src.lab2.rsa import *

class RSATestCase(unittest.TestCase):

    def test_is_prime(self):
        self.assertEqual(is_prime(0), False)
        self.assertEqual(is_prime(1), False)
        self.assertEqual(is_prime(2), True)
        self.assertEqual(is_prime(6), False)

    def test_gcd(self):
        self.assertEqual(gcd(10, 30), 10)
        self.assertEqual(gcd(6, 15), 3)
        self.assertEqual(gcd(9, 0), 9)
        self.assertEqual(gcd(5, 13), 1)

    def test_multiplicative_inverse(self):
        self.assertEqual(multiplicative_inverse(7, 40), 23)
        self.assertEqual(multiplicative_inverse(2, 25), 13)



if __name__ == '__main__':
    unittest.main()
