import os
from collections import defaultdict
from lxml import etree
import json


dir = os.path.dirname(__file__)

BASE_TAGS = ["NN", "NNP", "VB", "VBP", "JJ", "RB"]
STOPWORDS = os.path.join(dir, "data/stopwords.txt")
PATH_TO_SEMCOR = dir + "/data/semcor"


with open(STOPWORDS) as f1:
    stopwords = f1.read()

senses = defaultdict(list)

for filename in os.listdir(PATH_TO_SEMCOR):
    #if filename == "br-e01.xml" or filename == "br-e04.xml":
    xml = PATH_TO_SEMCOR + "/" + filename
    parser = etree.XMLParser(recover=True)
    tree = etree.parse(xml, parser)
    root = tree.getroot()
    context = root[0]
    all_sent = context.findall("p/s")

    for s in all_sent:
        context = []
        for word in s:
            try:
                w = word.attrib["lemma"]
                t = word.attrib["pos"]
                if t in BASE_TAGS and w not in stopwords:
                    context.append((w, t))
            except:
                pass
        for word in s:
            try:
                lemma = word.attrib["lemma"]
                tag = word.attrib["pos"]
                wn = word.attrib["wnsn"]
                #filter(context, lambda x: x[0] == lemma)
                filtered_context = [t for t in context if t[0]!=lemma]

                key = lemma + ":" + tag + ":" + wn

                if key in senses:
                    senses[key] += filtered_context
                else:
                    senses[key] = filtered_context
            except:
                pass

#
# with open("data/semcor_parsed.txt", "w+") as f:
#     for k, v in senses.items():
#         f.write(k + " ~ " + ', '.join(':'.join(elems) for elems in sorted(set(v))) + "\n")




