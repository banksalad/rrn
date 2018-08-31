import unittest
from datetime import date

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
        undecided, corresponding, not_corresponding = None, True, False
        female, male = True, False
        foreign, domestic = True, False

        for r, (b, s, f), expected in [
            ('RRN', (None, None, None), undecided),
            ('940812', (None, None, None), corresponding),
            ('940812', (None, male, None), undecided),
            ('940812', (None, None, foreign), undecided),
            ('940812', (None, female, foreign), undecided),
            ('8808121', (None, male, domestic), corresponding),
            ('6008122', (None, None, foreign), not_corresponding),
            ('7403225', (None, female, None), not_corresponding),
            ('9408131', (date(1994, 8, 13), None, None), corresponding),
            ('9408121', (date(1994, 8, 12), None, domestic), corresponding),
            ('0408127', (date(2004, 8, 12), male, domestic), not_corresponding),
            ('9408122', (date(1994, 8, 12), female, domestic), corresponding),
            ('9802145', (date(1998, 2, 14), male, foreign), corresponding),
            ('9103226', (date(1991, 3, 22), female, foreign), corresponding)
        ]:
            self.assertEqual(
                expected,
                rrn.is_corresponding_rrn(r, birthday=b, female=s, foreign=f)
            )
