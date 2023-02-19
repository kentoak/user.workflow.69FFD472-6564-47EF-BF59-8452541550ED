q = "{query}"
if q.startswith('up'):
	qs = q.split()
	print("up " + str(2 * int(qs[1]))),
elif q.startswith('down'):
	qs = q.split()
	print("down " + str(2 * int(qs[1]))),
else:
	print(q),
