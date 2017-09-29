import time
import math
import array
import sys

targetVariants = 5000
prevMax = 0

numbers = {}
for x in [2, 3]:
	numbers[x] = {}
	numbers[x]['is_prime'] = True
	numbers[x]['variations'] = []


def areVariationsEqual(lVal, rVal):
	# print("****")
	# print("lVal")
	# print(lVal)
	# print("rVal")
	# print(rVal)
	# print("****")
	if (len(rVal) != len(lVal)):
		return False
	for prime, count in lVal.items():
		if ((not prime in rVal) or (count != rVal[prime])):
			return False

	return True

def addVariation(dstValue, srcVariations):
	variationsToAdd = []
	# print("dst:")
	# print(numbers[dstValue]['variations'])
	# print("src:")
	# print(srcVariations)
	for srcVariation in srcVariations:
		add = True
		for dstVariation in numbers[dstValue]['variations']:
			if (areVariationsEqual(srcVariation, dstVariation)):
				add = False
				break
		if (add):
			variationsToAdd.append(srcVariation)
	numbers[dstValue]['variations'].extend(variationsToAdd)	

def mergeVarians(lVariants, rVariants):
	retval = []
	for lVariant in lVariants:
		for rVariant in rVariants:
			item = {}
			for x, count in lVariant.items():
				item[x] = count
			for x, count in rVariant.items():
				if (not x in item):
					item[x] = 0
				item[x] += count
			retval.append(item)
	# print("======")
	# print(lVariants)
	# print(rVariants)
	# print(retval)
	# print("======")
	return retval

currentNumber = 4
while True:
	isPrime = True
	for number, props in numbers.items():
		if (not props['is_prime']):
			continue
		else:
			if (currentNumber % number == 0):
				isPrime = False
				break

	numbers[currentNumber] = {}
	numbers[currentNumber]['is_prime'] = isPrime
	numbers[currentNumber]['variations'] = []

	# print ('--------')
	# print ('curent = %d' % currentNumber)
	for lv in xrange(2, currentNumber / 2 + 1):
		rv = currentNumber - lv
		# print ('rv = %d, lv = %d' % (lv, rv))
		# if (numbers[lv]['is_prime'] and numbers[rv]['is_prime']):
		# 	addVariation(currentNumber,
		# 		mergeVarians(
		# 			[{lv: 1}],
		# 			[{rv: 1}]
		# 			)
		# 		)
		lCurrentVariants = numbers[lv]['variations']
		rCurrentVariants = numbers[rv]['variations']
		if (numbers[lv]['is_prime']):
			lCurrentVariants = [{lv: 1}]
		if (numbers[rv]['is_prime']):
			rCurrentVariants = [{rv: 1}]

		if (len(lCurrentVariants) > 0 and len(rCurrentVariants) > 0):
			addVariation(
				currentNumber,
				mergeVarians(
					lCurrentVariants,
					rCurrentVariants
					)
				)


	if (len(numbers[currentNumber]['variations']) >= prevMax):
		print("=========")
		print("new max!")
		print("currentNumber: %d" % currentNumber)
		print("variations: %d" % len(numbers[currentNumber]['variations']))
		prevMax = len(numbers[currentNumber]['variations'])
		if (len(numbers[currentNumber]['variations']) >= targetVariants):
			print("WE HAVE A WINNER!")
			break
	currentNumber += 1
	

# print numbers
