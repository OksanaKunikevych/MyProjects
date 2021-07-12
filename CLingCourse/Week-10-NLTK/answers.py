from nltk import bigrams, trigrams, ngrams, WordNetLemmatizer, FreqDist
from nltk.corpus import wordnet as wn
from nltk.corpus import inaugural, names, stopwords, words, gutenberg
import random 


def get_keywords(input_file):
	"""Returns the semantic cloud of the input_file"""
	text = inaugural.words(input_file)
	text = [WordNetLemmatizer().lemmatize(w) for w.lower() in text \
	if w.isalpha() and w in words.words() \
	and w not in stopwords.words("english") and w not in names.words()]
	return FreqDist(text).most_common(15)

def generate_dict(left_context, right_context):
	"""Returns the list of words that occur in the specified context"""
	left = left_context.split()
	right = right_context.split()
	res = []
	ngram_len = len(left)+1+len(right)
	grams = ngrams(gutenberg.words(), ngram_len)
	for ngram in grams:
		if ngram[:len(left)]==tuple(left) and ngram[len(left)+1:]==tuple(right):
			res.append(ngram)
	fd = FreqDist(res)
	words = []
	for el in fd.most_common(len(fd.keys())):
		words.append(el[0][1])
	return words

def polysemy(input_file):
	"""Returns the average polysemy of the input_file"""
	with open(input_file, "r") as f:
		adj_words = f.read()
		num_senses, num_adj = 0, 0
		for word in adj_words.splitlines():
			if wn.synsets(word, pos=wn.ADJ)!=[]:
				num_adj +=1
				num_senses += len(wn.synsets(word, pos=wn.ADJ))
	return round(float(num_senses)/float(num_adj),2)

def generate_sentence(word):
	if word in gutenberg.words():
		sentence, grams = [], []
		for n in bigrams(gutenberg.words()):
			grams.append(n)
		def generate(word):
			sentence.append(word)
			if len(sentence)==40 or sentence[-1] in [".","?",";","!"]:
				return sentence
			else:
				res=[]
				for n in grams:
					if n[0]==word:
						res.append(n)
				fd=FreqDist(res)
				next_word=random.choice(fd.most_common(10))[0][1]
				generate(next_word)
		generate(word)
		return ' '.join(sentence)
	else:
		print "The sentence cannot be generated. Please, try another word."