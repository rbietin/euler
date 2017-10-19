N = 10000000

primeSieve = [1] * (N + 1)
primeSieve[0] = False
primeSieve[1] = False

print("starting building prime sieve...")

lastPrinted = 0
for i in xrange(2, len(primeSieve)):
	if (primeSieve[i]) == True:
		for j in xrange(2, N / i + 1):
			primeSieve[j * i] = False

print("done building prime sieve.")

primes = []
for i, x in enumerate(primeSieve):
	if (x):
		primes.append(i)

def distinctM():
	retval = 0
	for xInd in xrange(0, len(primes)):
		for yInd in xrange(xInd + 1, len(primes)):
			x = primes[xInd]
			y = primes[yInd]
			maxMul = 0
			if (x * y > N):
				break
			for i in xrange(1, 1000):
				mul1 = x ** i
				if (mul1 * y > N):
					break
				for j in xrange(1, 1000):
					mul = mul1 * (y ** j)
					if (mul > N):
						break
					if (mul > maxMul):
						maxMul = mul
			retval += maxMul
	return retval


print distinctM()