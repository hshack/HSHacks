import random
from nltk.corpus import wordnet
synsets = wordnet.synsets('wheedle')
words = []
word = []
for k in open('/usr/share/dict/three', 'r').read().split():
	if len(k) > 4:
		words.append(k)

while len(word) < 200:
	while True:
		try:
			choice = random.choice(words)
			synsets = wordnet.synsets(choice)
			x = synsets[0].definition
			break
		except:
			print 'ERROR!', choice
			words[words.index(choice):words.index(choice)+1] = ''			
	words[words.index(choice):words.index(choice)+1] = ''
	word.append(choice)


