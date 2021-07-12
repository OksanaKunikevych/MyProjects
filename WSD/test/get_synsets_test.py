import unittest
from Oksana.lesk import get_synsets


class TestGetSynsets(unittest.TestCase):
    def test_get_synsets(self):
        res = get_synsets("match", "NN")
        self.assertEqual(res,
                         ['match.n.01',
                               {(1, 'match.n.02'): [('compete', 'VBP'), ('contest', 'NN'), ('formal', 'JJ'),
                                                    ('person', 'NN'), ('team', 'NN')],
                                (2, 'match.n.03'): [('burning', 'JJ'), ('cardboard', 'NN'),
                                                    ('drop', 'VBP'), ('explode', 'VB'), ('match', 'NN'),
                                                    ('piece', 'NN'), ('place', 'NN'), ('whole', 'JJ'), ('wood', 'NN')],
                                (4, 'match.n.05'): [('match', 'NN'), ('score', 'NN'), ('win', 'VB')],
                                (7, 'couple.n.02'): [('chicago', 'NNP'), ('couple', 'NN'),
                                                     ('live', 'VBP'), ('married', 'JJ'), ('pair', 'NN'),
                                                     ('person', 'NN'), ('together', 'RB')],
                                (3, 'match.n.04'): [('duplicate', 'NN'), ('entry', 'NN'), ('exact', 'JJ'),
                                                    ('find', 'VB'), ('make', 'VB'), ('match', 'NN'), ('notebook', 'NN')],
                                (8, 'match.n.09'): [('good', 'JJ'), ('harmonize', 'VB'), ('jacket', 'NN'),
                                                    ('make', 'VB'), ('match', 'NN'), ('resemble', 'VB'), ('something', 'NN'), ('tie', 'NN')],
                                (6, 'peer.n.01'): [('equal', 'JJ'), ('group', 'NN'), ('person', 'NN'),
                                                   ('standing', 'NN')],
                                (0, 'match.n.01'): [('always', 'RB'), ('cardboard', 'NN'), ('carry', 'VB'),
                                                    ('chemical', 'NN'), ('combustible', 'JJ'), ('consist', 'VB'),
                                                    ('fag', 'NN'), ('friction', 'NN'), ('ignite', 'VB'),
                                                    ('light', 'JJ'), ('light', 'NN'), ('light', 'VB'), ('long', 'RB'),
                                                    ('lucifer', 'NN'), ('match', 'NN'), ('piece', 'NN'), ('pipe', 'NN'),
                                                    ('thin', 'JJ'), ('tip', 'VB'), ('wood', 'NN')],
                                (5, 'catch.n.03'): [('good', 'JJ'), ('matrimonial', 'JJ'), ('person', 'NN'),
                                                    ('prospect', 'NN'), ('regard', 'VB')]}])

if __name__ == '__main__':
    unittest.main()