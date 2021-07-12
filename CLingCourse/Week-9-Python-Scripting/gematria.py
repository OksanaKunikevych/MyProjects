# Gematria
# By Oksana Kunikevych

"""
Gematria.

Counts the numeric value of the word according to the given letter_values.

"""

import sys, re


letter_values_1 = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':80, 'g':3, 'h':8,
'i':10, 'j':10, 'k':20, 'l':30, 'm':40, 'n':50, 'o':70, 'p':80, 'q':100,
'r':200, 's':300, 't':400, 'u':6, 'v':6, 'w':800, 'x':60, 'y':10, 'z':7}

letter_values_2 = {"a":6, "b":12, "c":18, "d":24, "e":30, "f":36, "g":42, 
"h":48, "i":54, "j":60, "k":66, "l":72, "m":78, "n":84, "o":90, "p":96,
"q":102, "r":108, "s":114, "t":120, "u":126, "v":132, "w":138, "x":144,
"y":150, "z":156}

def count_gematria (word, option):
	gematria = 0
	v1, v2 = [letter_values_1][-1], [letter_values_2][-1]
	for letter in word.lower():
		if option == 1:
			gematria += v1[letter]
		if option == 2:
			gematria += v2[letter]
	return gematria

def decode(text, option):
	gematria_dict = {}
	text = text.lower().split()
	for word in text:
		if word.isalpha():
			gematria = count_gematria(word, option)
			if gematria in gematria_dict:
				gematria_dict[gematria].add(word)
			else:
				gematria_dict[gematria] = {word}
	return gematria_dict

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print "Usage: python gematria.py <input file> <output file> <option (1 or 2)>"
    if sys.argv[3] not in ["1","2"]:
    	print "There are only two options. Please choose 1 or 2."
    else:
    	input_f = open(sys.argv[1],'r').read()
    	output_f = open(sys.argv[2],'a')
        decoded = decode(input_f,int(sys.argv[3]))
        for key in sorted(decoded):
        	output_f.write(str(key)+': '+' '.join(decoded[key])+'\n')