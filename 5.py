dividerCounts = {}
maxNum = 20

for i in xrange(2, maxNum + 1):
	dividerCounts[i] = 0

	for j in xrange(2, i + 1):
		counter = 0
		while i % j == 0:
			counter += 1
			i /= j
		if counter > dividerCounts[j]:
			dividerCounts[j] = counter

retval = 1

for idx, val in dividerCounts.items():
	retval *= idx ** val

print retval