import unittest
import Q2.FindBiggerString as fbs


class TestsForStrings(unittest.TestCase):

    # -------------------TESTS for Greater Function-----------------------
    def test1_ForGreater(self):
        res = fbs.greater('1.1', '1.2')
        self.assertEqual(res, False)

    def test2_ForGreater(self):
        res = fbs.greater('-1.1', '-1.2')
        self.assertEqual(res, True)

    def test3_ForGreater(self):
        res = fbs.greater('1.1', '0')
        self.assertEqual(res, True)

    def test4_ForGreater(self):
        res = fbs.greater('1.1', '-1.1')
        self.assertEqual(res, True)

    def test5_ForGreater(self):
        res = fbs.greater('0', '-0')
        self.assertEqual(res, False)

    # -------------------TESTS for Lesser Function-------------------------
    def test1_ForLesser(self):
        res = fbs.lesser('1.1', '1.2')
        self.assertEqual(res, True)

    def test2_ForLesser(self):
        res = fbs.lesser('-1.1', '-1.2')
        self.assertEqual(res, False)

    def test3_ForLesser(self):
        res = fbs.lesser('1.1', '0')
        self.assertEqual(res, False)

    def test4_ForLesser(self):
        res = fbs.lesser('1.1', '-1.1')
        self.assertEqual(res, False)

    def test5_ForLesser(self):
        res = fbs.lesser('0', '-0')
        self.assertEqual(res, False)

    # ------------TESTS for Equal Function-----------------------------
    def test1_ForEqual(self):
        res = fbs.equal('1.1', '1.2')
        self.assertEqual(res, False)

    def test2_ForEqual(self):
        res = fbs.equal('1.1', '1.1')
        self.assertEqual(res, True)

    def test3_ForEqual(self):
        res = fbs.equal('1.1', '0')
        self.assertEqual(res, False)

    def test4_ForEqual(self):
        res = fbs.equal('1.1', '-1.1')
        self.assertEqual(res, False)

    def test5_ForEqual(self):
        res = fbs.equal('0', '-0')
        self.assertEqual(res, True)

unittest.main()