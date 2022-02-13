import re
chars = []
with open("./15_6_valid_exp.txt", "r") as pos_file:
	for line in pos_file:
		chars.append(pos_file.readline())
no_chars = ['2','+','6','3']
yes_chars = ['1','\-','0','4','5','7','8','9','*','/']

x = re.compile('^['+"".join(no_chars)+']+$')
y = re.compile('^['+"".join(yes_chars)+']+$')
curr = []
for i in chars:
	if re.search(x,i) or not re.search(y,i):
		print("Valid: ", i)
		curr.append(i)

print(len(curr))