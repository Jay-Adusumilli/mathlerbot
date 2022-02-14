import re

def remove():
	x = re.compile('^['+"".join(no_chars)+']+$')
	y = re.compile('^['+"".join(yes_chars)+']+$')
	curr = []
	for i in chars:
		if re.search(x,i) or not re.search(y,i):
			print("Valid: ", i)
			curr.append(i)
	return curr

answer_list = []
with open("./15_6_valid_exp.txt", "r") as pos_file:
	for line in pos_file:
		answer_list.append(pos_file.readline())
no_chars = []
yes_chars = ['0','1','2','3','4','5','6','7','8','9','+','\-','*','/']
