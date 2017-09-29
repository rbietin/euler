maxTiels = 10**6

possibleLaminas = []
for x in xrange(2, maxTiels / 4):
	possibleLaminas.append(x * 4)

retval = 1

for i in xrange(0, len(possibleLaminas)):
	used = 0
	# print ('--------')
	for j in xrange(i, len(possibleLaminas), 2):
		used += possibleLaminas[j]
		if (used > maxTiels):
			break
		# print possibleLaminas[j]
		retval += 1

print retval