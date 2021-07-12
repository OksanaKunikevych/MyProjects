import re

def exclamate (sentence):
	"""Returns exclamated sentence"""
	if sentence[len(sentence) - 1] == "?":
		if sentence[1].isupper():
			return [sentence[1]]+[sentence[0].lower()]+sentence[2:len(sentence)-1]+["!"]
		else:
			return [sentence[1].capitalize()]+[sentence[0].lower()]+sentence[2:len(sentence)-1]+["!"]
	else: return "Sorry, I can't answer this question"

def british_colours(word):
	"""Returns BrE variant of the word 'color'"""
	return word.replace("color", "colour")

def is_palindrome(word):
	"""Returns True if given word is pallindrome"""
	return word.lower()==word.lower()[::-1]

def is_valid (password):
	"""Returns True if the password is valid"""
	return len (password)>=8 and password.isalnum() \
	and len (re.findall('\d', password))==2 and len (re.findall('[A-Z]',password))==2

def the_longest_common_prefix (w1, w2):
	"""Returns the longest common prefix of two words: w1 and w2"""
	prefix = ""
	for i in range(min(len(w1), len(w2))):
		if w1[i]==w2[i]:
			prefix += w1[i]
		else:
			return prefix
	return prefix

def parse_math_problems(sentence):
	"""Returns solved mathematical problem from parsed sentence"""
	sentence = sentence.lower()
	numbers = map(int, re.findall('\d+', sentence))
	if numbers == []:
		return "No problems found."
	elif "multiply" in sentence:
		 return reduce(lambda a,b: a*b, numbers)
	elif "add" in sentence:
		 return sum(numbers)
	elif "subtract" in sentence:
		 return reduce(lambda a,b:b-a, numbers)
	elif "divide" in sentence:
		 return reduce(lambda a,b: a/b, numbers)

def number_of_articles(input_file):
	import re
	"""Returns the average number of articles per sentence"""
	num=0 
	articles=['a','an','the']
	f=open(input_file, 'r').read().splitlines()
	for line in f:
		for word in line.split():
			if word.lower() in articles:
				num+=1
	return float(num)/len(f)

def real_zen(input_file):
	"""Prints out the input_file in nice format"""
	num = 0
	fl = open(input_file)
	f = fl.read().splitlines()
	for line in f:
		if line.startswith("Author:"):
			print "by " + line[len("Author: "):]
		if line.startswith("Title:"):
			print line[len("Title: "):]
	for line in f:
		if not line.startswith("//") and not line.startswith("Title:") and not line.startswith("Author:"):
			num += 1
			print str(num) + ". " + line

def form_dictionary(input_file, output_file):
  """Returns an output_file with transformational dictionary of set expressions"""
  with open(input_file, 'r') as input_f:
    with open(output_file, 'w') as output_f:
      for line in input_f:
         words = line.split()
         line = line.rstrip('\r\n')
         if "a" in words:
              output_f.write(line.replace(" a "," ") + ' ~ ' + line + '\n')
              output_f.write(line.replace(" a "," the ") + ' ~ ' + line + '\n')
         elif "an" in words:
              output_f.write(line.replace(" an "," ") + ' ~ ' + line + '\n')
              output_f.write(line.replace(" an "," the ") + ' ~ ' + line + '\n')
         elif "the" in words:
              output_f.write(line.replace(" the "," ") + ' ~ ' + line + '\n')
              if words[words.index("the") + 1][0] in "aeoui":
                 output_f.write(line.replace(" the "," an ") + ' ~ ' + line + '\n')
              else:
                 output_f.write(line.replace(" the "," a ") + ' ~ ' + line + '\n')
def find_genes(genome):
  """Returns an array of all genes in the GENOME"""
  exception = ["ATG", "TAG", "TAA", "TGA"]
  gene = []
  g = re.findall("(?<=ATG).*?(?=TAA|TAG|TGA)", genome)
  gene.append([a for a in g if len(a)%3 == 0 and a not in exception])
  return gene

