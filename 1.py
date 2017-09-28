numbers = [0, 3, 5, 6, 9, 10, 12]

retval = 0
stop = False


while not stop:
	for i in xrange(0, len(numbers)):
		if (numbers[i] >= 1000):
			stop = True
			break
		retval += numbers[i]
		print numbers[i]
		numbers[i] += 15

print retval