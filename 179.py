maxTarget = 10 ** 7


sieve = [0] * (maxTarget + 2)
retval = 0
for i in xrange(1, maxTarget + 1):
	for j in xrange(1, (maxTarget) / i + 1):
		sieve[j * i] += 1
	# print "%d->\t%d" % (i, sieve[i])
	# print "-%d->%d" % (i + 1, sieve[i + 1])
	if (sieve[i] == sieve[i + 1] + 1):
		retval += 1
		# print "i : %d" %i
		# # print "sieve[i] : %d" %sieve[i]
		# # print "sieve[i+1] : %d" %sieve[i+1]

print retval