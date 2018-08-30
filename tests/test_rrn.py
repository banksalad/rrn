import unittest

import rrn


class TestRRN(unittest.TestCase):

    def test_is_valid_rrn(self):
        valid, invalid = True, False
        for s, expected in [
            (None, invalid),
            ('', invalid),
            ('RRN', invalid),
            ('9', valid),
            ('94', valid),
            ('940', valid),
            ('941', valid),
            ('942', invalid),
            ('8808', valid),
            ('9413', invalid),
            ('94081', valid),
            ('94023', invalid),
            ('94022', valid),
            ('94084', invalid),
            ('940833', invalid),
            ('940812', valid),
            ('940228', valid),
            ('960228', valid),
            ('960229', valid),
            ('960230', invalid),
            ('000001-2', invalid),
            ('9408122', valid),
            ('940812200', valid),
            ('940812299', invalid),
            ('9408121001745', valid),
            ('9408121001749', invalid),
            ('9408121001751', valid),
            ('9408121001750', invalid),
            ('9408221001740', valid),
            ('9408221001741', invalid)
        ]:
            self.assertEqual(expected, rrn.is_valid_rrn(s))

    def test_is_corresponding_rrn(self):
        self.assertEqual(1 + 1, 2)
