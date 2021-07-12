from collections import defaultdict

import math
from nltk.corpus import wordnet as wn

import logging
import os

# from Oksana.scripts.data_parser import parse
# from Oksana.scripts.get_ngram_cling import get_ngram
# from Oksana.scripts.tokenize_cling import tag_text

from data_parser import parse
from get_ngram_cling import get_ngram
from tokenize_cling import tag_text


dir = os.path.dirname(__file__)

BASE_TAGS = ["NN", "NNP", "VB", "VBP", "JJ", "RB"]
TAGS_MAPPING = {"n":"NN", "v":"VB", "a":"JJ", "s":"JJ", "r":"RB"}
WORDFORMS = os.path.join(dir, "data/word-forms.txt")
STOPWORDS = os.path.join(dir, "data/stopwords.txt")
SEMCOR = os.path.join(dir, "data/semcor_parsed.txt")

FILENAME = "data/test-set.txt"

# config logger
LOG_FILENAME = 'lesk_logs.log'
FORMAT = "%(asctime)s %(message)s"
logging.basicConfig(filename=LOG_FILENAME, format=FORMAT, level=logging.INFO)
logger = logging.getLogger(__name__)



wf = defaultdict(tuple)
semcor = defaultdict(list)

with open(WORDFORMS) as f:
    for line in f:
        k, v = line.split(" ~ ")
        wf[k] = v.strip()

with open(STOPWORDS) as f1:
    stopwords = f1.read()


with open(SEMCOR) as f2:
    for line in f2:
        k, v = line.split(" ~ ")
        semcor[k] = [tuple(x.split(":")) for x in v.split(", ")]

def lemmatize(wt):
    key = wt[0].lower() + ":" + wt[1]
    if wf[key]:
        val, k = wf[key].split(":")
        return (k, val)
    else:
        return wt

#print(lemmatize(('insisting', 'VBG')))
#print(lemmatize(('i', 'PRP')))

def get_context (sentence):
    words = tag_text(sentence)[0]
    context = []
    for word in words:
        lemma = lemmatize(word)
        if lemma[0] not in stopwords and lemma[1] in BASE_TAGS:
            context.append(lemma)
    return set(context)

#print(get_context(["firm worker"]))
#print(get_context(["not soft or yielding to pressure"]))


def normalize_tag(tag):
    for k, v in TAGS_MAPPING.items():
            tag = tag.replace(v, k)
    return tag


def get_synsets(word, tag):
    #print((word, tag))
    orig_wt = (word, tag)
    tag = normalize_tag(tag)
    synsets = wn.synsets(word, pos=tag)
    first_sense = synsets[0].name()
    wn_context = defaultdict(list)
    counter = 1
    for synset in synsets:
        definition = get_context([synset.definition()])
        examples = get_context([" ".join(synset.examples())])
        context_all = sorted(definition.union(examples))
        # remove original word from context
        if orig_wt in context_all: context_all.remove(orig_wt)
        synset_name = (counter, synset.name())
        counter+=1
        wn_context[synset_name] = context_all
    return [first_sense, wn_context]

if __name__ == '__main__':
    logger.info('Start evaluating ' + FILENAME + " ...")
    d = parse(FILENAME)
    tp, fp = 0, 0
    for item in d:
        intersections = []
        # Tag sentence
        s = tag_text([" ".join(item["sentence"])])[0]
        sentence_orig = [lemmatize(wt) for wt in s]

        # Get error index
        idx = list(item["senses"].keys())[0]

        # Get ambig_word from sentence
        ambig_word = lemmatize(sentence_orig[idx])
        correct_sense = list(item["senses"].values())[0]

        # Get wordnet context for each sense
        default_sense, wn_context = get_synsets(ambig_word[0], ambig_word[1])


        # Count intersection for each sense with original sentence
        for sense, context in wn_context.items():
            w = []

            # Get additional context from SemCor
            semcor_context = semcor[ambig_word[0] + ":" + ambig_word[1] + ":" + str(sense[0])]

            all_context = context + semcor_context
            common = (list(set(all_context).intersection(set(sentence_orig))))
            count_intersect = (len(common))

            #print(sense, common, ambig_word)
            for el in common:
                w.append(float(get_ngram("prob:" + el[0]).strip()))

            weighted_intersect = sum(w)

            intersections.append((count_intersect, # use either weighted_intersect or count_intersect
                                  sense[0], sense[1]))

            #print(sense, common)
        # Get sense that has the highest number of intersections
        sorted_senses = sorted(intersections, key=lambda tup:(-tup[0], tup[1]))

        if sorted_senses[0][0] == 0:
            top_sense = default_sense
        else:
            top_sense = sorted_senses[0][2]

        logger.info(correct_sense + "   " + top_sense)

        # Evaluate model
        if correct_sense == top_sense:
            tp += 1
        else:
            fp += 1
    prec = round((tp / (tp + fp)) * 100, 4)
    logger.info("==================================")
    logger.info("TP: %s" % tp)
    logger.info("FP: %s" % fp)
    logger.info("Precision: %s" % prec)
    logger.info("==================================")
    logger.info("\n")


