import unittest
from datetime import date

import rrn


class TestRRN(unittest.TestCase):

    def test_is_foreign(self):
        undetermined = None
        foreign, domestic = True, False
        for s, expected in [
            ('', undetermined),
            ('9', undetermined),
            ('94', undetermined),
            ('940', undetermined),
            ('9408', undetermined),
            ('94081', undetermined),
            ('940812', undetermined),
            ('9408120', domestic),
            ('94081201', domestic),
            ('9408121', domestic),
            ('94081212', domestic),
            ('9408122', domestic),
            ('94081223', domestic),
            ('9408123', domestic),
            ('94081234', domestic),
            ('9408124', domestic),
            ('94081245', domestic),
            ('9408125', foreign),
            ('94081256', foreign),
            ('9408126', foreign),
            ('94081267', foreign),
            ('9408127', foreign),
            ('94081278', foreign),
            ('9408128', foreign),
            ('94081289', foreign),
            ('9408129', domestic),
            ('94081290', domestic)
        ]:
            self.assertEqual(expected, rrn.is_foreign(s))

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
            ('9408221001741', invalid),
            ('9408225', valid),
            ('940822699', valid),
            ('940822700888', valid),
            ('9408228008889', valid)
        ]:
            self.assertEqual(expected, rrn.is_valid_rrn(s))

    def test_is_corresponding_rrn(self):
        corresponding, not_corresponding = True, False
        female, male = True, False
        foreign, domestic = True, False

        for r, (b, s, f), expected in [
            ('RRN', (None, None, None), not_corresponding),
            ('940812', (None, None, None), corresponding),
            ('940812', (None, male, None), corresponding),
            ('940812', (None, None, foreign), corresponding),
            ('940812', (None, female, foreign), corresponding),
            ('8808121', (None, male, domestic), corresponding),
            ('6008122', (None, None, foreign), not_corresponding),
            ('7403225', (None, female, None), not_corresponding),
            ('9408131', (date(1994, 8, 13), None, None), corresponding),
            ('9408121', (date(1994, 8, 12), None, domestic), corresponding),
            ('0408127', (date(2004, 8, 12), male, domestic), not_corresponding),
            ('9408122', (date(1994, 8, 12), female, domestic), corresponding),
            ('9802145', (date(1998, 2, 14), male, foreign), corresponding),
            ('9103226', (date(1991, 3, 22), female, foreign), corresponding),
            ('620904', (date(1962, 9, 4), male, domestic), corresponding),
            ('6209041', (date(1962, 9, 4), male, domestic), corresponding)
        ]:
            self.assertEqual(
                expected,
                rrn.is_corresponding_rrn(r, birthday=b, female=s, foreign=f)
            )
