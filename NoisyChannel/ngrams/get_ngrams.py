# -*- coding: utf-8 -*-
import spell_parser
from collections import defaultdict


print "Reading data ..."
txt = spell_parser.spell_parse("data/misspelled-train.txt")
words = []
for item in txt:
    words += item["corrections"].values()

unigrams = defaultdict(int)
bigrams = defaultdict(int)
for w in words:
    w = "^"+w.lower()+"$"
    for i in range(len(w) - 1):
        unigrams[w[i]] += 1
        bigrams[w[i]+w[i+1]] += 1

with open("unigrams.txt", "w") as f1:
    for k, v in sorted(unigrams.items()):
        f1.write(k+":"+str(v)+"\n")

with open("bigrams.txt", "w") as f2:
    for k, v in sorted(bigrams.items()):
        f2.write(k+":"+str(v)+"\n")

