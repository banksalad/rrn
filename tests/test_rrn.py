import unittest

import rrn


class TestRRN(unittest.TestCase):

    def test_is_valid_rrn(self):
        with self.assertRaises(ValueError):
            rrn.is_valid_rrn('940812 is my birthday')

        s = '9-408-12'
        for i in range(len(s)):
            with self.assertRaises(ValueError):
                rrn.is_valid_rrn(s[:i])

        for expected, s in [
            (True, '940812'),
            (False, '000001-2'),
            (True, '9408122'),
            (True, '940812200'),
            (False, '940812299'),
            (True, '9408121001745'),
            (False, '9408121001749'),
            (True, '9408121001751'),
            (False, '9408121001750'),
            (True, '9408221001740'),
            (False, '9408221001741')
        ]:
            self.assertEqual(expected, rrn.is_valid_rrn(s))

    def test_is_corresponding_rrn(self):
        self.assertEqual(1 + 1, 2)
