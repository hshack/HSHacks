from termcolor import colored, cprint
import random, math
score = 0
pos = 0
global full
full = 0
real = open('/usr/share/dict/words').read().split() #Added files to my computer
fake = open('/usr/share/dict/fake').read().split()
fake = sorted(set(fake))
def draw():
	for k in range(0, 3):
		print ''

def check(var):
#	print var.split()
	for k in var.split():
#		print k
		if k in prof:
			return True
#		else:
#			return False
draw()
cprint('YOU HAVE STARTED WORD LEARNING! CONGRATULATIONS!', 'red')
draw()
cprint('This test will give you random words, and you have to say whether they are real or not.', 'yellow')
draw()
cprint("Hit ENTER when you're ready! Good luck!", 'cyan')
raw_input()
for k in range(1, 11):
	num = random.randint(1, 2)
	if num == 1:
		word = random.choice(real)
		cprint('Is %s a real word?' %(word.lower()), 'blue')
		var = raw_input()
		if var.lower().startswith('y') == True:
			cprint('Yes!', 'green')
			score+=1
		elif var.lower().startswith('n') == True
			cprint('No!', 'red')
		pos+=1
		full = (int((float(score)/float(pos))*100))
		cprint('Your score so far is %d%%!' %(full), 'cyan')
	else:
		word = random.choice(fake)
		cprint('Is %s a real word?' %(word.lower()), 'blue')
		var = raw_input()
	        if var.lower().startswith('n') == True and check(var) != True:
	                cprint('Yes!', 'green')
			score+=1
	        elif var.lower().startswith('y') == True and check(var) != True:
	                cprint('No!', 'red')
		else:
			var = var.split()
                        for k in var:
                                if k in prof:
                                        print 'You too!'
                                        break
			cprint('STOP CUSSING!', 'magenta')
		pos+=1
		full = (int((float(score)/float(pos))*100))
                cprint('Your score so far is %d%%!' %(full), 'cyan')

def evaluate():
	global full
	if full <= 20:
		level = 1
	elif full > 20 and full <= 40:
		level = 2
	elif full > 40 and full <= 60:
		level = 3
	elif full > 60 and full <= 80:
		level = 4
	else:
		level = 5
	return int(level)

