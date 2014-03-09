from termcolor import cprint, colored
from getpass import getpass
from pickle import dump, load
from nltk.corpus import wordnet
from os import system
import time, sys, random
learned = 0
num = 1
today = []
wrong = []
dict = {}
print ''
print ''
print ''
cprint('YOU HAVE ENTERED WORD LEARNING!', 'red')
print ''
print ''
print ''
cprint('Please enter your credentials:\n', 'cyan')
cprint('Username:\n', 'green')
usr = raw_input()
print '\n'
cprint('Password:\n', 'green')
password = getpass('')
print '\n'
try:
	info = load(open("%s.p" %(usr), "rb"))
	username, password, level, words = info
	if info[1] == password:
		print 'Hello %s! You are level %d in Word Learning!' %(info[0], info[2])
	else:
		print "I'm sorry, but that is the incorrect password for %s. Try again later!" %(usr)
except IOError:
	import start
	print "Calculating your stats..."
	time.sleep(2)
	x = start.evaluate()
	x = int(x)
	print "You are level %d!" %(x)
	import getthree
	words = getthree.word
	username = usr
	level = x
	info = [username, password, level, words]
	dump(info, open("%s.p" %(usr), "wb"))
	print 'Here are your words: '
	for k in words:
		print '%d. %s' %(num, k)
		num+=1

for k in words:
	synsets = wordnet.synsets(k)
	dict[k] = synsets[0].definition

copy = list(words)
for k in range(0, 5):
	choice = random.choice(copy)
	today.append(choice)
	del(copy[copy.index(choice)])

for k in today:
	cop = list(copy)
	for i in range(0, 4):
		choice = random.choice(cop)
		wrong.append(dict[choice])
		del(cop[cop.index(choice)])
	cprint('Your word is:', 'green')
	cprint(k, 'red')
	system('say your word is %s' %(k))
	time.sleep(1)
	cprint('The definition of %s is:'%(k), 'blue')
	cprint(dict[k], 'magenta')
	defin = dict[k].replace(' (', ', ').replace(')', '')
	system('say The definition of %s is %s' %(k, defin))
	time.sleep(4)
	for f in range(1, 8):
		print '\n'
	randnum = random.randint(0, 4)
	wrong.insert(randnum, dict[k])
	print 'What is the definition of %s?' %(k)
	for j in range(1, 6):
		print '%d. %s' %(j, wrong[j-1])
	var = int(raw_input())
	if var-1 == randnum:
		print 'Correct!'
	else:
		print 'No, %s means %s' %(k, dict[k])
		system('say No, %s means %s' %(k, dict[k]))
