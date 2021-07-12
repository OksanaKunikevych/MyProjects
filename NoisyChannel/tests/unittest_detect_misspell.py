# -*- coding: utf-8 -*-
from eval_oksana import detect_misspell
from tokenize_cling import tokenize
import unittest


class TestFactorial(unittest.TestCase):
    """
    Our basic test class
    """

    def test_detect_misspell(self):
        res = detect_misspell(tokenize(["This is a trest."])[0])
        self.assertEqual(res, [3])
        res = detect_misspell(tokenize(["Tori Spelling is a versatile acress whose career spans theater, television and film."])[0])
        self.assertEqual(res, [5])
        res = detect_misspell(tokenize(["Melania liked Mrs. O alot."])[0])
        self.assertEqual(res, [4])
        res = detect_misspell(tokenize(["Diving across the finish line shouldnt be allowed."])[0])
        self.assertEqual(res, [5])
        res = detect_misspell(tokenize(["Diving across the finish line shouldmt be allowed."])[0])
        self.assertEqual(res, [5])
        res = detect_misspell(tokenize(["I don't usually shy away from openended questions."])[0])
        self.assertEqual(res, [7])
        res = detect_misspell(tokenize(["I don't usally shy away from openended questions."])[0])
        self.assertEqual(res, [3, 7])


if __name__ == '__main__':
    unittest.main()