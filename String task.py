k = str(input()).lower()
s=""
L = ['a','e','i','o','u','y']
for i in range(0,len(k)):
	if k[i] not in L:
		s+='.'+k[i]			
print(s)