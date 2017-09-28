prev = 2
cur = 8

retval = 2

while cur < 4 * 10**6:
	retval += cur
	new = prev + cur * 4
	prev = cur
	cur = new

print retval