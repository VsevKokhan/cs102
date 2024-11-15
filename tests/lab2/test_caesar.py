import unittest

from src.lab2.caesar import *


class CaesarTestCase(unittest.TestCase):
    def test_encrypt_caesar(self):
        self.assertEqual(encrypt_caesar('hello'), 'khoor')
        self.assertEqual(encrypt_caesar('ITMO'), 'LWPR')
        self.assertEqual(encrypt_caesar('ITMO', 4), 'MXQS')
        self.assertEqual(encrypt_caesar('stu', 5), 'xyz')
        self.assertEqual(encrypt_caesar(''), '')

    def test_decrypt_caesar(self):
        self.assertEqual(decrypt_caesar('khoor'), 'hello')
        self.assertEqual(decrypt_caesar('LWPR'), 'ITMO')
        self.assertEqual(decrypt_caesar('MXQS', 4), 'ITMO')
        self.assertEqual(decrypt_caesar('xyz', 5), 'stu')
        self.assertEqual(decrypt_caesar(''), '')

if __name__ == '__main__':
    unittest.main()
