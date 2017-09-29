import time
import math
import array


maxPrime = 100
maxTarget = 10 ** 9

primeSieve = bytearray([1] * (maxTarget + 1)) #[True] * (maxTarget + 1)
primeSieve[0] = False
primeSieve[1] = False

print("starting building prime sieve...")

lastPrinted = 0
for i in xrange(2, len(primeSieve)):
	if (primeSieve[i]) == True:
		if (time.time() - lastPrinted > 1):
			print i
			lastPrinted = time.time()
		for j in xrange(2, maxTarget / i + 1):
			primeSieve[j * i] = False

print("done building prime sieve.")

targetSieve = [False] * (maxTarget + 1)

for i in xrange(1, maxPrime + 1):
	targetSieve[i] = True

print("starting building target sieve...")

for i in xrange(2, maxPrime + 1):
	if (primeSieve[i]):
		for j in xrange(1, maxTarget / i + 1):
			if ((not targetSieve[j]) or (j > maxPrime and primeSieve[j])):
				continue
			tmp = i * j
			targetSieve[tmp] = True

print("done building target sieve.")

# for idx, val in enumerate(targetSieve):
# 	if (val):
# 		print idx
retval = 0
for x in targetSieve:
	if x:
		retval += 1

print 'retval: %d' % retval
