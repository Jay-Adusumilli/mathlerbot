import re
chars = ["111111","222222","333333","444444","5555555", "6666666", "77777777"]
no_chars = ['1','2','6']
yes_chars = ['3', '4']

x = re.compile('^['+"".join(no_chars)+']+$')
y = re.compile('^['+"".join(yes_chars)+']+$')
for i in chars:
	if re.search(x,i) or not re.search(y,i):
		print("Valid: ", i)