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

# NAMES ARRAY 
boys_arr = [ 
	"James", 
	"John", 
	"Robert", 
	"Michael", 
	"William", 
	"David", 
	"Richard", 
	"Joseph", 
	"Thomas", 
	"Charles", 
	"Christopher", 
	"Daniel", 
	"Matthew", 
	"Anthony", 
	"Donald",  
	"Mark", 
	"Paul", 
	"Steven", 
	"Andrew", 
	"Kenneth", 
	"Joshua", 
	"George", 
	"Kevin", 
	"Brian", 
	"Edward", 
	"Ronald", 
	"Timothy", 
	"Jason", 
	"Jeffrey", 
	"Ryan", 
	"Jacob", 
	"Gary", 
	"Nicholas", 
	"Eric", 
	"Stephen", 
	"Jonathan", 
	"Larry", 
	"Justin", 
	"Scott", 
	"Brandon", 
	"Frank", 
	"Benjamin", 
	"Gregory", 
	"Samuel", 
	"Raymond", 
	"Patrick", 
	"Alexander", 
	"Jack", 
	"Dennis", 
	"Jerry", 
	"Tyler", 
	"Aaron", 
	"Jose", 
	"Henry", 
	"Douglas", 
	"Adam", 
	"Peter", 
	"Nathan", 
	"Zachary", 
	"Walter", 
	"Kyle", 
	"Harold", 
	"Carl", 
	"Jeremy", 
	"Keith", 
	"Roger", 
	"Gerald", 
	"Ethan", 
	"Arthur", 
	"Terry", 
	"Christian", 
	"Sean", 
	"Lawrence", 
	"Austin", 
	"Joe", 
	"Noah", 
	"Jesse", 
	"Albert", 
	"Bryan", 
	"Billy", 
	"Bruce", 
	"Willie", 
	"Jordan", 
	"Dylan", 
	"Alan", 
	"Ralph", 
	"Gabriel", 
	"Roy", 
	"Juan", 
	"Wayne", 
	"Eugene", 
	"Logan", 
	"Randy", 
	"Louis", 
	"Russell", 
	"Vincent", 
	"Philip",
	"Bobby", 
	"Johnny", 
	"Bradley" 
	]

girls_arr = [
	"Mary", 
	"Patricia", 
	"Jennifer", 
	"Linda", 
	"Elizabeth", 
	"Barbara", 
	"Susan", 
	"Jessica", 
	"Sarah", 
	"Karen",
	"Nancy", 
	"Margaret", 
	"Lisa", 
	"Betty", 
	"Dorothy", 
	"Sandra", 
	"Ashley", 
	"Kimberly", 
	"Donna", 
	"Emily", 
	"Michelle", 
	"Carol", 
	"Amanda", 
	"Melissa", 
	"Deborah", 
	"Stephanie", 
	"Rebecca", 
	"Laura", 
	"Sharon", 
	"Cynthia", 
	"Kathleen", 
	"Helen", 
	"Amy", 
	"Shirley", 
	"Angela", 
	"Anna", 
	"Brenda", 
	"Pamela", 
	"Nicole", 
	"Ruth", 
	"Katherine", 
	"Samantha", 
	"Christine", 
	"Emma", 
	"Catherine", 
	"Debra", 
	"Virgina", 
	"Rachel", 
	"Carolyn", 
	"Janet", 
	"Maria", 
	"Heather", 
	"Diane", 
	"Julie", 
	"Joyce", 
	"Victoria",  
	"Christina",
	"Kelly"
	"Joan", 
	"Evelyn", 
	"Lauren", 
	"Judith", 
	"Olivia", 
	"Frances", 
	"Martha", 
	"Cheryl", 
	"Megan", 
	"Andrea", 
	"Hannah", 
	"Jacqueline", 
	"Ann", 
	"Jean", 
	"Alice", 
	"Kathryn"
	"Gloria", 
	"Teresa", 
	"Doris", 
	"Sara", 
	"Janice", 
	"Julia", 
	"Marie", 
	"Madison", 
	"Grace", 
	"Judy", 
	"Theresa", 
	"Beverly", 
	"Denise", 
	"Marilyn", 
	"Amber", 
	"Danielle", 
	"Abigail", 
	"Brittany", 
	"Rose", 
	"Diana", 
	"Natalie",
	"Sophia", 
	"Alexis", 
	"Lori", 
	"Kayla", 
	"Jane"
]

surnames_arr = [
	"Smith", 
	"Johnson", 
	"Williams", 
	"Brown", 
	"Jones", 
	"Miller", 
	"Davis", 
	"Garcia", 
	"Rodriguez", 
	"Wilson", 
	"Martinez", 
	"Anderson", 
	"Taylor",
	"Thomas", 
	"Hernandez", 
	"Moore", 
	"Martin", 
	"Jackson", 
	"Thompson", 
	"White", 
	"Lopez", 
	"Lee", 
	"Gonzalez", 
	"Harris", 
	"Clark", 
	"Lewis", 
	"Robinson", 
	"Walker", 
	"Perez", 
	"Hall", 
	"Young", 
	"Allen", 
	"Sanchez", 
	"Wright", 
	"King", 
	"Scott", 
	"Green", 
	"Baker", 
	"Adams", 
	"Nelson", 
	"Hill", 
	"Ramirez", 
	"Campbell", 
	"Mitchell", 
	"Roberts", 
	"Carter", 
	"Phillips", 
	"Evans", 
	"Turner", 
	"Torres", 
	"Parker",
	"Collins", 
	"Edwards", 
	"Stewart", 
	"Flores", 
	"Morris", 
	"Nguyen", 
	"Murphy", 
	"Rivera", 
	"Cook", 
	"Rogers", 
	"Morgan", 
	"Peterson", 
	"Cooper", 
	"Reed", 
	"Bailey", 
	"Bell", 
	"Gomez", 
	"Kelly", 
	"Howard", 
	"Ward", 
	"Cox", 
	"Diaz",
	"Richardson", 
	"Wood", 
	"Watson", 
	"Brooks", 
	"Bennett", 
	"Gray", 
	"James", 
	"Reyes", 
	"Cruz", 
	"Hughes", 
	"Price", 
	"Myers", 
	"Long", 
	"Foster", 
	"Sanders", 
	"Ross", 
	"Morales", 
	"Powell", 
	"Sullivan", 
	"Russell", 
	"Ortiz", 
	"Jenkins", 
	"Gutierrez", 
	"Perry", 
	"Butler", 
	"Barnes", 
	"Fisher"
]

surnames_arr1 = [
	"Tremblay", 
	"Gagnon", 
	"Roy", 
	"Bouchard", 
	"Gauthier", 
	"Morin", 
	"Lavoie", 
	"Fortin", 
	"Hernandez", 
	"Mora", 
	"Rodriguez", 
	"Gonzalez", 
	"Jimenez", 
	"Morales", 
	"Sanchez", 
	"Ramirez", 
	"Perez", 
	"Calderon", 
	"Gutierrez", 
	"Rojas", 
	"Vargas", 
	"Torres", 
	"Salas", 
	"Segura", 
	"Valverde", 
	"Villalobos", 
	"Araya", 
	"Herrera", 
	"Lopez", 
	"Madrigal", 
	"Garcia", 
	"Martinez",
	"Diaz", 
	"Fernandez", 
	"Alvarez", 
	"Reyes", 
	"Pena", 
	"Rosario", 
	"Santana", 
	"Nunez", 
	"Castillo", 
	"De la Cruz", 
	"Curz", 
	"Guzman", 
	"Gomez", 
	"Santos", 
	"Fuentes", 
	"Vasquez", 
	"De Los Santos", 
	"Mejia", 
	"Ponce", 
	"Montes", 
	"Flores", 
	"Rivera", 
	"Rivas", 
	"Ramos", 
	"Portillo", 
	"Escobar", 
	"Orellana", 
	"Romero", 
	"Aguilar", 
	"Alvarado", 
	"Estrada", 
	"Mendez", 
	"Velasquez", 
	"Ruiz", 
	"Ortiz", 
	"Alvarez", 
	"Chavez", 
	"Medina", 
	"Castro", 
	"Contreras", 
	"Luna", 
	"Dominquez", 
	"Garza", 
	"Soto", 
	"Espinoza", 
	"Juarez", 
	"Vega", 
	"Cervantes", 
	"Silva", 
	"Rios", 
	"Navarro", 
	"Delgado", 
	"Solis", 
	"Valdez"
]

"""
https://en.wikipedia.org/wiki/List_of_most_common_surnames_in_North_America
"""
name_arr = boys_arr + girls_arr

def testAccuracies(programType="both"):

	if programType not in ["both", "NLTK", "nltk", "SpaCy", "spacy"]:
		return "Please use a current program type: both, NLTK, nlkt, SpaCy, spacy"

	# Test Accuracy 
	nltk_count = 0 
	spacy_count = 0

	for name in name_arr: 
		# Seems NLTK depends on capitalization to distinguish between "NN" and "NNP"
		name = name.lower()

		if (programType == "NLTK" or programType == "nltk" or programType == "both"):
			############################
			# NLTK
			############################
			#print("STARTING NLTK")
			ex = name + " is new  \n"
			#ex += "okay memento meet " + name + " who is a new face" 
			#ex += "okay memento " + name + " is a new face \n"
			#ex += "hi " + name + " nice to meet you \n"
			#ex += name + " nice to meet you \n"
			#ex += "nice to meet you " + name + " \n"
			#ex += "okay memento say hello to " + name + " \n" 

			def preprocess(sent):
				sent = nltk.word_tokenize(sent)
				sent = nltk.pos_tag(sent)
				return sent

			sent = preprocess(ex)

			# Find all NNP tagged entities 
			get_names_nltk = []
			for i in range(0, len(sent)):
				if sent[i][1] == 'NNP':
					get_names_nltk.append(sent[i][0])
			#print("NLTK: ", get_names_nltk)
			if len(get_names_nltk) > 0: 
				nltk_count += 1

		if (programType == "SpaCy" or programType == "spacy" or programType == "both"):
			############################
			# SpaCy
			############################
			#print("STARTING SPACY")
			#ex = name + " is a new person \n"                        # %53
			#ex += "okay memento meet " + name + " who is a new face" # %51
			ex = "okay memento " + name + " is a new face \n"     	  # %68
			#ex += "hi " + name + " it is nice to meet you \n"      	# %48
			#ex += name + " it is nice to meet you \n"             		# %39
			#ex += "it is nice to meet you " + name + " \n"         	# %45
			#ex += "okay memento say hello to " + name + " \n"      	# %25

			doc = nlp(ex)

			named_entities = [(X.text, X.label_) for X in doc.ents]

			# Find all PERSON tagged entities 
			get_names_spacy = []
			for i in range(len(named_entities)):
				if named_entities[i][1] == 'PERSON':
					get_names_spacy.append(named_entities[i][0])
			#print("SpaCy: ", get_names_spacy)
			if len(get_names_spacy) > 0: 
				spacy_count += 1

	print("NLTK Accuracy: ", float(nltk_count)/float(len(name_arr)) * 100)
	print("SpaCy Accuracy: ", float(spacy_count)/float(len(name_arr)) * 100)


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
		return list(set(names))[0].split(" ")
	else:
		return list(set(names))


##########################
# TEST DRIVER 
##########################
# Comparing NLTK and SpaCy
# testAccuracies()

# Test Extraction Function
# 88.01515151515152
# "The new name is " + name  + " " + last + " I know that " + name  + " " + last +  " is a new person so please add " + name  + " " + last + " to the database "
count = 0
for name in name_arr:
	for last in surnames_arr:
		hello = extractName("The new name is " + name  + " " + last + " so please add " + name  + " " + last + " to the database ", "spacy")
		if len(hello) == 2:
			#print(hello)
			count += 1
print(count)
print((count/ (len(name_arr) * len(surnames_arr))) * 100)

				


