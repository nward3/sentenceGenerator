# author: Nick Ward
# date: 2/25/16
# This project uses the ideas of markov chains to randomly generate English sentences

from collections import defaultdict
import random

# generates a dictionary with the probabilities based on the markov
# model order to use as a foundation for sentence generation
def load_text(sample_text, order):
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

# determines the desired markov model order used to generate sentences
def get_order():
	try:
		order = int(raw_input("Select a markov model order 1-10: "))
		if order > 10 or order < 1:
			print "Try again: the number must be an integer between 1-10"
			order = get_order()
	except ValueError:
		print "Try again: the number must be an integer between 1-10"
		order = get_order()
	return order

# determines the desired text file to use as input for markov model
def get_textfile(order):
	print "Select a number representing one of the following input files to base sentence generation on:"
	print "Robin Hood:              1"
	print "Tom Sawyer:              2"
	print "Pride and Prejudice:     3"
	print "Alice in Wonderland:     4"
	print "A Tale of Two Cities:    5"
	try:
		inputfile = int(raw_input("Specify an input file to base sentence generation on: "))
		if inputfile > 5 or inputfile < 1:
			print "Try again: specify a valid input file designated by the corresponding number"
			print ""
			print ""
			inputfile = get_textfile(order)
	except ValueError:
		print "Try again: specify a valid input file designated by the corresponding number"
		print ""
		print ""
		inputfile = get_textfile(order)
	return inputfile

if __name__ == "__main__":
	# possible sources of text
	texts = {1: "texts/rh.txt", 2: "texts/ts.txt", 3: "texts/pp.txt", 4: "texts/aw.txt", 5: "texts/ttc.txt"}
	order = get_order()
	text_number = get_textfile(order)
	text = load_text(texts[text_number], order)

	# determine the initial seed toi start sentence generation
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

