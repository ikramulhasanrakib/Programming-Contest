word = input()
up=0
low=0
for char in word:
	if char.isupper():
		up+=1
	else:
		low+=1
if up>low:
	print(word.upper())
else:
	print(word.lower())
	