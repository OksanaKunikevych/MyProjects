import unittest
from Oksana.lesk import get_context


class TestGetContext(unittest.TestCase):
    def test_get_context_1(self):
        res = get_context(["not soft or yielding to pressure"])
        self.assertEqual(res, {('yield', 'VB'), ('soft', 'JJ'), ('pressure', 'NN')})

    def test_get_context_2(self):
        res = get_context(["the science concerned with the study of physical objects and substances"])
        self.assertEqual(res, {('substance', 'NN'), ('object', 'NN'), ('physical', 'JJ'), ('science', 'NN'),
                               ('study', 'NN'), ('concern', 'VB')})

    def test_get_context_3(self):
        res = get_context([""])
        self.assertEqual(res, {})

if __name__ == '__main__':
    unittest.main()