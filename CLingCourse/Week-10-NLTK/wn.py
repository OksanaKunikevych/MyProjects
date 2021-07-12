# Wordnet info
# by Oksana K.


""""
Prints out the Wordnet info about the given WORD.
"""


import sys
from nltk.corpus import wordnet as wn


def wordnet(word):
	num_synsets = len(wn.synsets(word))
	def synonyms(word, s):
		synset = wn.synsets(word)[s]
		synonyms = [item for item in synset.lemma_names() if item!=word]
		if synonyms!=[]:
			print("It has the following synonyms:", ", ".join(synonyms))

	def antonyms(word, s):
		synset = wn.synsets(word)[s]
		ant = [item for item in synset.antonyms() if item != word]
		if ant != []:
			print("It has the following antonyms:", ", ".join(ant))

	def examples(word,s):
		word = wn.synsets(word)[s]
		if word.examples()!=[]:
			print ("Typical examples of usage:", "\n", "\n".join(
                word.examples()))
	def hypernyms(word,s):
		word = wn.synsets(word)[s].hypernyms()
		res = []
		if word!=[]:
			for syn in word:
				res.append(syn.name()[:-5])
		if res!=[]:
			print ("Hypernyms:", ' '.join(res))
	def hyponyms(word,s):
		word = wn.synsets(word)[s].hyponyms()
		res = []
		if word!=[]:
			for syn in word:
				res.append(syn.name()[:-5])
		if res!=[]:
			print ("Hyponyms:", ' '.join(res))
	def meronyms (word,s):
		word = wn.synsets(word)[s].part_meronyms()
		res = []
		if word!=[]:
			for syn in word:
				res.append(syn.name()[:-5])
		if res!=[]:
			print ("Meronyms:", ' '.join(res))
	def holonyms (word,s):
		word = wn.synsets(word)[s].member_holonyms()
		res = []
		if word!=[]:
			for syn in word:
				res.append(syn.name()[:-5])
		if res!=[]:
			print ("Holonyms:", ' '.join(res))
	def print_info(word,i):
			synonyms(word, i)
			examples(word,i)
			hypernyms(word,i)
			hyponyms(word,i)
			meronyms(word,i)
			holonyms(word,i)
	for i in range(num_synsets):
		if wn.synsets(word)[i].pos()=='n':
			print (i+1, '. ' 'NOUN:', wn.synsets(word)[i].definition())
			print_info(word,i)
		if wn.synsets(word)[i].pos()=='v':
			print (i+1, '. ' 'VERB:', wn.synsets(word)[i].definition())
			print_info(word,i)
		if wn.synsets(word)[i].pos()=='a':
			print (i+1, '. ' 'ADJECTIVE:', wn.synsets(word)[i].definition())
			print_info(word,i)
		if wn.synsets(word)[i].pos()=='r':
			print (i+1, '. ' 'ADVERB:', wn.synsets(word)[i].definition())
			print_info(word,i)

#
#
# if __name__ == '__main__':
#     if len(sys.argv) != 2:
#             print ("Usage: wn_info.py <word>")
#     else:
#             if wn.synsets(sys.argv[1])==[]:
#                 print ("Sorry, there is no such word in Wordnet.")
#             else:
#                 wordnet(sys.argv[1])




def get_antonyms(word):
	all_antonyms, t = [], []
	for sense in wn.synsets(word):
		if sense.pos() in ['a', 's', 'r']:
			for ant in sense.lemmas():
				all_antonyms.append(ant.name())
		for a in all_antonyms:
			if a not in t:
				t.append(a)
	return t





print(get_antonyms("smart"))