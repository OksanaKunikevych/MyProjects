import nltk, re
from nltk import *
from nltk.corpus import *


#Have Them All Covered

grammar = nltk.CFG.fromstring("""
    TOP -> S | SBARQ
	S -> NP VP | NP VP PERIOD | NP2 VP QUESTION
	SQ -> VP
	SBARQ -> SBAR COMMA WHNP SQ QUESTION
	NP -> DT NN | DT JJ NN
	NP2 -> NP SBAR
	SBAR -> S | IN S
	VP -> VBP | VBP NP | VBN ADVP | VBD VP | VBG PP | VBZ NP 
	PP -> IN NP
	WHNP -> WP
	ADVP -> RB
	DT -> "The" | "the"
	JJ -> "old"
	NN -> "man" | "old" | "boat" | "ship"
	VBP -> "man"
	VBZ -> "mans"
	VBD -> "was"
	VBN -> "sold"
	VBG -> "rocking"
	IN -> "in" | "If"
	RB -> "yesterday"
	WP -> "who"
	COMMA -> ","
	QUESTION -> "?"
	PERIOD -> "."
	""")