import re
filename = input("Enter name of the text file: ")
f = open(filename, 'r')
text = f.read()
words = set(text.split())
words_mulset = text.split()
horror = open('horror.txt', 'r')
text1 = horror.read()
chk_words = text1.splitlines()
word_counts = dict()
horror_score = 0
ratio = 1 
wt_sci_fi=1*ratio
wt_horror=1*ratio
wt_action=1*ratio
wt_comedy=2*ratio
wt_drama=1*ratio
wt_roman=1*ratio
wt_fan=1*ratio
for w in chk_words:
	x=w.split()
	word_counts[x[0]] = len(re.findall(x[0], text, re.I))
	horror_score = horror_score + word_counts[x[0]]*int(x[-1])*wt_horror
# sci-fi
sci_fi = open('sci-fi.txt', 'r')
text1 = sci_fi.read()
chk_words = text1.splitlines()
word_counts = dict()
sci_fi_score = 0
for w in chk_words:
	x=w.split()
	word_counts[x[0]] = len(re.findall(x[0], text, re.I))
	sci_fi_score = sci_fi_score + word_counts[x[0]]*int(x[-1])*wt_sci_fi
# comedy

comedy = open('comedy.txt', 'r')
text1 = comedy.read()
chk_words = text1.splitlines()
word_counts = dict()
comedy_score = 0
for w in chk_words:
	x=w.split()
	word_counts[x[0]] = len(re.findall(x[0], text, re.I))
	comedy_score = comedy_score + word_counts[x[0]]*int(x[-1])*wt_comedy
#drama
drama = open('drama.txt', 'r')
text1 = drama.read()
chk_words = text1.splitlines()
word_counts = dict()
drama_score = 0
for w in chk_words:
	x=w.split()
	word_counts[x[0]] = len(re.findall(x[0], text, re.I))
	drama_score = drama_score + word_counts[x[0]]*int(x[-1])*wt_drama

#action

action = open('action.txt', 'r')
text1 = action.read()
chk_words = text1.splitlines()
word_counts = dict()
action_score = 0
for w in chk_words:
	x=w.split()
	word_counts[x[0]] = len(re.findall(x[0], text, re.I))
	action_score = action_score + word_counts[x[0]]*int(x[-1])*wt_action

#fantasy

fantasy = open('fantasy.txt', 'r')
text1 = fantasy.read()
chk_words = text1.splitlines()
word_counts = dict()
fantasy_score = 0
for w in chk_words:
	x=w.split()
	word_counts[x[0]] = len(re.findall(x[0], text, re.I))
	fantasy_score = fantasy_score + word_counts[x[0]]*int(x[-1])*wt_fan

#romantic

romantic = open('romantic.txt', 'r')
text1 = romantic.read()
chk_words = text1.splitlines()
word_counts = dict()
romantic_score = 0
for w in chk_words:
	x=w.split()
	word_counts[x[0]] = len(re.findall(x[0], text, re.I))
	romantic_score = romantic_score + word_counts[x[0]]*int(x[-1])*wt_roman

#output
max_ans=horror_score+drama_score+sci_fi_score+romantic_score+fantasy_score+action_score+comedy_score
print("Movie genres:")
if (5*horror_score>=max_ans):
	print("horror")
if (4*sci_fi_score>=max_ans) and sci_fi_score>=300:
	print("sci-fi")
if (4*action_score>=max_ans) or action_score >=175:
	print("action")
if (5*fantasy_score>=max_ans):
	print("fantasy")
if (5*romantic_score>=max_ans):
	print("romantic")
if (5*comedy_score>=max_ans):
	print("comedy")
if (5*drama_score>=max_ans) or drama_score >=150:
	print("drama")

