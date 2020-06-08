import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
import spacy
from spacy import displacy
from collections import Counter
import en_core_web_sm
nlp = en_core_web_sm.load()
from nltk.chunk import conlltags2tree, tree2conlltags
from pprint import pprint
from bs4 import BeautifulSoup
import requests
import re


def extractName(text, programType="both"):
	text = text.lower()
	names = []

	if (programType == "NLTK" or programType == "nltk" or programType == "both"):
				tokenized = nltk.word_tokenize(text)
				tagged = nltk.pos_tag(tokenized)
				for i in range(0, len(tagged)):
					if tagged[i][1] == 'NNP':
						names.append(tagged[i][0])

	if (programType == "SpaCy" or programType == "spacy" or programType == "both"):
				processed = nlp(text)
				named_entities = [(X.text, X.label_) for X in processed.ents]
				for i in range(len(named_entities)):
					if named_entities[i][1] == 'PERSON':
						names.append(named_entities[i][0])
	if len(list(set(names))) != 0: 
		foundNames = list(set(names))[0].split(" ")
		nameStr = ""
		for name in foundNames:
			nameStr += name + " "
		return nameStr
	else:
		return " "

				


