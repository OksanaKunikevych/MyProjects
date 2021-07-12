# -*- coding: utf-8 -*-
import re
from tokenize_cling import tokenize

CORRECTION = re.compile(r"\w[\w'-]+\{[\w '-]+\}")


def spell_parse(filename):
    """
    Parse the spellchecker test and train corpora.
    :param filename: str
    :return: list of dicts
            {'corrections': {id: correction}, 'sentence':[list of tokens]}
    """
    with open(filename, "r") as f:
        tokens = tokenize([re.sub(r"(\w[\w'-]+)\{[\w '-]+\}", r"\1", line)
                           for line in f.readlines()])
    data = []
    with open(filename, "r") as f:
        i = 0
        for line in f.readlines():
            spans = [m.span() for m in re.finditer(CORRECTION, line)]
            corrections = [line[b:e].strip("}").split("{") for b, e in spans]
            mapping = {}
            prev = -1
            for orig,corr in corrections:
                prev = tokens[i].index(orig, prev + 1)
                mapping[prev] = corr
            data.append({"sentence": tokens[i], "corrections": mapping})
            i += 1
    return data


# d = spell_parse("data/misspelled-test.txt")
# print d