# author: Nick Ward
# date: 2/25/16
# This project uses the ideas of markov chains to randomly generate English sentences

from collections import defaultdict
import random

# generates a dictionary with the probabilities based on the markov
# model order and textfile as a foundation for sentence generation
def load_textfile(sample_text, order):
	text = defaultdict(list)

	while order > 0:
		f = open(sample_text, 'r')
		for line in f:
			line = line.rstrip()
			i = 0
			while i < len(line):
				if i < len(line) - order:
					text[line[i:i + order]].append(line[i + order])
				i += 1
		f.close()
		order -= 1

	return text

# generates a dictionary with the probabilities based on the markov
# model order and user text as a foundation for sentence generation
def load_usertext(user_text, order):
	text = defaultdict(list)

	while order > 0:
		user_text = user_text.rstrip()
		i = 0
		while i < len(user_text):
			if i < len(user_text) - order:
				text[user_text[i:i + order]].append(user_text[i + order])
			i += 1
		order -= 1
	
	return text

# determines the desired markov model order used to generate sentences
def get_order():
	try:
		order = int(raw_input("Select a markov model order 1-10: "))
		if order > 10 or order < 1:
			print "Try again: the number must be an integer between 1-10"
			print ""
			order = get_order()
	except ValueError:
		print "Try again: the number must be an integer between 1-10"
		print ""
		order = get_order()
	return order

# determines the desired text file to use as input for markov model
def get_text(order):
	print "Select a number from the list to base sentence generation on:"
	print "Type your own text:      1"
	print "Robin Hood:              2"
	print "Tom Sawyer:              3"
	print "Pride and Prejudice:     4"
	print "Alice in Wonderland:     5"
	print "A Tale of Two Cities:    6"
	try:
		inputfile = int(raw_input("Specify an input file to base sentence generation on: "))
		if inputfile > 6 or inputfile < 1:
			print "Try again: specify a valid input file designated by the corresponding number"
			print ""
			inputfile = get_text(order)
	except ValueError:
		print "Try again: specify a valid input file designated by the corresponding number"
		print ""
		inputfile = get_text(order)
	return inputfile

if __name__ == "__main__":
	# possible sources of text
	texts = {2: "texts/rh.txt", 3: "texts/ts.txt", 4: "texts/pp.txt", 5: "texts/aw.txt", 6: "texts/ttc.txt"}
	order = get_order()
	text_number = get_text(order)

	# get text and create dictionary for character generation
	if text_number == 1:
		user_text = ""
		print "Enter your text below: (A blank line ends input)"
		for line in iter(raw_input, ''):
			user_text += line
		text = load_usertext(user_text, order)
	else:
		text = load_textfile(texts[text_number], order)

	# determine the initial seed to start sentence generation
	max = 0
	index = ""
	sentence = ""
	newchar = ""
	for key in text.keys():
		if len(text[key]) > max and len(key) == order and key[0].isupper():
			max = len(text[key])
			index = key
			newchar = random.choice(text[index])
	
	sentence += newchar
	index = index[1:] + newchar

	# generate text until the max size is reached or text generator cannot predict the next character
	temporder = order
	while len(sentence) < 1000 and temporder > 0:
		if index[-temporder:] in text.keys():
			newchar = random.choice(text[index[-temporder:]])
			index = index[1:] + newchar
			sentence += newchar
			temporder = order
		else:
			temporder -= 1
	print ""
	print "Generated Text:"
	print sentence

