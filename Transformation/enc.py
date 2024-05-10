f = open('enc', 'r')
for i in f:
	print(i.encode('utf-16-be'))