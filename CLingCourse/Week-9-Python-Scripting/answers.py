from __future__ import division
import re

def ari(input_file):
  """Returns the Automated Readability Index of the INPUT_FILE"""
  f = open(input_file, 'r').read()
  sentences = f.split('\n')
  words = f.split()
  chars = sum(len(w) for w in words)
  chars_per_word = chars/len(words)
  words_per_sent = len(words) / len(sentences)
  return round(4.71 * chars_per_word + 0.5 * words_per_sent - 21.43, 2)

def lexical_diversity(input_file):
	"""Returns the lexical diversity of the INPUT_FILE"""
	f = open(input_file, 'r').read()
	words = f.lower().split()
	unique = set(words)
	return round(len(unique) * 100 /len(words),2 )

def to_pig_latin(word):
	"""Returns the WORD converted into Pig Latin"""
	return re.sub(r"(^(y(?=[aeuio])|[^aoeyi]*)|(?<!u))([a-z]*$)", r"\3\2ay",word.lower())

def tokenize(sentence):
	"""Returns tokenized SENTENCE"""
	punctuation = re.compile(r"((?<!(\s|[A-Z]))((\.)(?=($|\"$))|((?<!(\d))\,)|\:|\;|\&|\!|\?|\(|\)|\[|\]|\{|\}|\"))")
	quotes = re.compile(r"((\"|\(|\[)(?=\w))")
	contractions = re.compile(r"(?<!\s)('ll|'d|'s|'re|n't|'m)")
	numbers = re.compile(r"(\$?\d+(\,\d+)?)")
	s = re.sub(punctuation,r" \1",sentence)
	s = re.sub(quotes,r"\1 ",s)
	s = re.sub(contractions,r" \1",s)
	s = re.sub(numbers,r" \1",s)
	return s