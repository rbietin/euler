def isPalindrome(x):
	tmp = int(x)
	mirror = 0
	while tmp != 0:
		mirror = 10 * mirror + (tmp % 10)
		tmp = tmp / 10
	return mirror == x

retval = 0

for i in xrange(100, 1000):
	for j in xrange(i, 1000):
		tmp = i * j
		if (tmp > retval and isPalindrome(tmp)):
			retval = tmp
			# print "i: %d, j: %d" % (i,j)

print retval

