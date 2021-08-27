def clean_word(word):
	if word[:3] == "'''":
		word = word[3:]
	if word[-4:] == "''',":
		word = word[:-4]
	if word == "'''":
		word = ""
	return word


import random
import numpy as np
import os

folder = "hp"
sources = os.listdir(folder)

words = {}

for source in sources:

	f = open(folder + "/" + source, 'r', encoding="utf8")

	lines = f.readlines()

	for line in lines:
		line_words = line.split(" ")
		for i in range(len(line_words)):
			word = clean_word(line_words[i].strip())
			if word not in words.keys():
				words[word] = []
			if i != len(line_words) - 1:
				next_word = clean_word(line_words[i+1].strip())
				if next_word != '':
					words[word].append(next_word)

choice = int(random.random()*len(words.keys()))

keys = list(words.keys())

out = keys[choice]

word_count = 1
word = keys[choice]
next_words = words[word]

while len(next_words) != 0:
	choice = int(random.random()*len(next_words))
	word = next_words[choice]
	out += " " + word
	next_words = words[word]
	word_count += 1

print(out)