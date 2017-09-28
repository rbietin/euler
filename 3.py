number = 600851475143

factor = 2

while True:
	if (factor < number):
		if (number % factor == 0):
			number /= factor
		else:
			factor += 1
	else:
		break

print factor