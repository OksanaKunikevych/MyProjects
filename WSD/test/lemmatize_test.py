import unittest
from Oksana.lesk import lemmatize


class TestLemmatize(unittest.TestCase):
    def test_lemmatize(self):
        res = lemmatize(("sleeping", "VBG"))
        self.assertEqual(res, ("sleep", "VB"))
    def test_lemmatize_same_lemma(self):
        res = lemmatize(("flower", "NN"))
        self.assertEqual(res, ("flower", "NN"))
    def test_lemmatize_unknown(self):
        res = lemmatize(("frlowrs", "NNS"))
        self.assertEqual(res, None)




if __name__ == '__main__':
    unittest.main()