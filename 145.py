
maxNumber = 10 ** 9

def isReversiable(number):
	if (number % 10 == 0):
		return False
	reversedNumber = 0
	tmp = number
	while (tmp != 0):
		reversedNumber *= 10
		reversedNumber += tmp % 10
		tmp /= 10

	tmp = reversedNumber + number
	while tmp != 0:
		if ((tmp % 10) % 2 == 0):
			return False
		tmp /= 10
	return True

retval = 0
for x in xrange(1, maxNumber + 1):
	if (x % (maxNumber / 100) == 0):
		print "processed: %d%%. Already found: %d" % (100 * x / maxNumber, retval)
	if (isReversiable(x)):
		retval += 1

print "retval: %d" % retval