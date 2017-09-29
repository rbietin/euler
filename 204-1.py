import time
import math
import array
import sys

maxPrime = 100
maxTarget = 10 ** 9

# maxPrime = 5
# maxTarget = 10 ** 8

primeSieve = bytearray([1] * (maxPrime + 1))
primeSieve[0] = False
primeSieve[1] = False

print("starting building prime sieve...")

lastPrinted = 0
for i in xrange(2, len(primeSieve)):
	if (primeSieve[i]) == True:
		for j in xrange(2, maxPrime / i + 1):
			primeSieve[j * i] = False

print("done building prime sieve.")

grid = {}

for idx, val in enumerate(primeSieve):
	if (val):
		grid[idx] = [1]
		power = 2
		tmp = idx
		while tmp < maxTarget:
			grid[idx].append(tmp)
			tmp = idx ** power
			power += 1

targetVals = []

indexes = {}
for k, v in grid.items():
	indexes[k] = 0
lastIncreased = 0

def nextIndex():
	for i,val in indexes.items():
		indexes[i] += 1
		lastIncreased = i
		if (indexes[i] >= len(grid[i])):
			indexes[i] = 0
		else:
			return True

	return False

retval = 1

while nextIndex():
	tmp = 1
	add = True
	for idx, val in indexes.items():
		tmp *= grid[idx][val]
		if (tmp > maxTarget):
			add = False
			break

	if (add):
		retval += 1

		if (retval % 10000 == 0):
			print retval
			print "indexes"
			for idx, val in indexes.items():
				if (val):
					print "%d**%d" % (idx, val)		

	else:
		for i in xrange(0, lastIncreased):
			indexes[i] = 99999




print retval
