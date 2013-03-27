from unittest import TestCase
from collections import namedtuple
from calc_margins import calc_margins


Column = namedtuple('Column', 'name width')


class TestMarginsForOneColumn(TestCase):

    def setUp(self):

        A = Column('A', 50)
        self.s = [A]
        self.fl = [A]
        self.cl = self.s[:]

    def test_margins_for_one_column_is_0(self):

        expected_margin = [0]
        actual_margin = calc_margins(self.cl, self.fl, self.s)
        self.assertEqual(expected_margin, actual_margin)


class TestMarginsForTwoColumns(TestCase):

    def setUp(self):
        pass

    def test_cl_equal_fl(self):

        A = Column('A', 50)
        B = Column('B', 25)

        s = [A, B]
        fl = [A, B]
        cl = s[:]

        expected_margins = [0, 0]
        actual_margins = calc_margins(cl, fl, s)
        self.assertEqual(expected_margins, actual_margins)

    def test_cl_not_equal_fl(self):

        A = Column('A', 50)
        B = Column('B', 25)

        s = [A, B]
        fl = [B, A]
        cl = s[:]

        expected_margins = [25, -75]
        actual_margins = calc_margins(cl, fl, s)
        self.assertEqual(expected_margins, actual_margins)


class TestMarginsForThreeColumns(TestCase):

    def setUp(self):

        self.A = Column('A', 50)
        self.B = Column('B', 35)
        self.C = Column('C', 15)
        self.s = [self.A, self.B, self.C]
        self.cl = self.s[:]

    def test_A_B_C(self):

        fl = [self.A, self.B, self.C]

        expected_margins = [0, 0, 0]
        actual_margins = calc_margins(self.cl, fl, self.s)
        self.assertEqual(expected_margins, actual_margins)

    def test_A_C_B(self):

        fl = [self.A, self.C, self.B]

        expected_margins = [0, 15, -50]
        actual_margins = calc_margins(self.cl, fl, self.s)
        self.assertEqual(expected_margins, actual_margins)

