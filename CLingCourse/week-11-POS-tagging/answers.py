import nltk, re
from nltk import *
from nltk.corpus import brown
from cPickle import dump

#1

data = brown.tagged_sents(categories="romance")
size = int(len(data) * 0.9)
train_set = data[:size]
test_set = data[size:]

patterns = [('.*ing$', 'VBG'),
			(".*ize$" ".*ate$" ".*ify$" ".*fy$", "VB"),
			('.*ed$', 'VBD'), 
			('.*es$', 'VBZ'), 
			('.*ould$', 'MD'), 
			(".*\\'s$", 'NN$'), 
			(".*al$" ".*[ae]nce$" ".*a?tion$" ".*ment$" ".*ness$" ".*ism$"
			 ".*ery$" "[ae]nt$" ".*ee$" ".*ist$" "[aeo]r$", "NN"),
			(".*ly$", 'RB'),
			('.*s$', 'NNS'),
			("^[A-Z].*$", "NP"),
			("^[A-Z].*e?s$", "NPS"),
			(".*able$" ".*al$" ".*ant$" ".*ary$" ".*ent$" 
				".*est$" ".*ful$" ".*ible$" ".*ic$" ".*ing$"
				".*ish$" ".*ive$" ".*less$" ".*ous$", 'JJ'),
			('^-?[0-9]+(.[0-9]+)?$', 'CD'), 
			('.*', 'NN'),
			('.*ier$', 'JJR'), 
			('.*iest$', 'JJS')]
t0 = RegexpTagger(patterns)
t1 = UnigramTagger(train_set, backoff=t0)
t2 = BigramTagger(train_set, backoff=t1)
t3 = TrigramTagger(train_set, backoff=t2)
print t3.evaluate(test_set)

#3

def extracting_adjectives(input_file):
	"""Returns a list of adjectives that can be used in the given construction"""
	regex = re.compile("\\b[Aa]n?_DT (\S+)_JJ \S+_CD \S+_NNS\\b")
	data = open(input_file, "r").read()
	adj = re.findall(regex, data)
	return sorted(set(adj))

#4 

def extracting_sents(input_file):
	"""Returns a list of sentences that can be used in the given construction"""
	sent = []
	data = open(input_file, 'r')
	regex = re.compile("^.*\w_PRP\$ \w+_VBG \w+_DT.*$")
	for s in data:
		if re.findall(regex, s):
		   sent.append(' '.join([word.split('_')[0] for word in s.split()]))
		   sent = [w.replace("-LRB-", "(") for w in sent]
		   sent = [w.replace("-RRB-", ")") for w in sent] 
	return sent

#5

def most_ambiguous(input_file):
	"""returns the word(s) that has/have the biggest number of different tags"""
	mydict = defaultdict(set)
	num = 0 
	word = []
	data = open(input_file, "r").read()
	for tagged in data.split():
			wt = tagged.split("_")
			mydict[wt[0]].add(wt[1])
	for i in mydict.keys():
		lenght = len(set(mydict[i]))
		if lenght > num:
			num = lenght
			word = [i]
		elif lenght == num:
			word.append(i)
	return word