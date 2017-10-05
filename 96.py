# THIS CODE IS A MESS
#
# Physical Considerations:
# WARNING! For safety, you should be in a good health
# and free from high blood pressure, heart, back or 
# neck problems, motion sickness, or other conditions
# that could be aggravated by this adventure. Expectant
# mothers should NOT read this code
#
# read on your oun risk. i'll refactor it. later. someday. maybe.

import copy
import sys
from sets import Set
puzzles = []

unsolvables = Set()

with open('data/p096_sudoku.txt', 'r') as f:
	puzzle = [[0,0,0,0,0,0,0,0,0] for i in range(9)]
	lineCount = 0
	for line in f:
		line = line.strip()
		if (len(line) != 9):
			continue
		for j in xrange(0, len(line)):
			puzzle[lineCount][j] = int(line[j])
		lineCount += 1
		if (lineCount % 9 == 0):
			puzzles.append(puzzle)
			puzzle = [[0,0,0,0,0,0,0,0,0] for i in range(9)]
			lineCount = 0

def getAsString(puzzle):
	retval = ""
	for i in xrange(0, 9):
		for j in xrange(0, 9):
			retval += str(puzzle[i][j])
		retval += "\n"
	return retval

def getVariants(i, j, puzzle):
	vertical = [True] * 10
	horizontal = [True] * 10
	quad = [True] * 10
	for k in xrange(0, 9):
		vertical[puzzle[k][j]] = False
		horizontal[puzzle[i][k]] = False

	i_quad = i / 3
	j_quad = j / 3

	for i1 in xrange(3 * i_quad, 3 * i_quad + 3):
		for j1 in xrange(3 * j_quad, 3 * j_quad + 3):
			quad[puzzle[i1][j1]] = False

	retval = []
	
	for k in xrange(1,10):
		if (vertical[k] and horizontal[k] and quad[k]):
			retval.append(k)

	return retval

def normalizeAssumption(i, j, assumpions):
	target = assumpions[i][j]
	if (isinstance(target, list)):
		checkSets = []
		row = []
		for x in xrange(0,9):
			if (x != j and isinstance(assumpions[i][x], list)):
				row.append(assumpions[i][x])
		checkSets.append(row)
		col = []
		for x in xrange(0,9):
			if (x != i and isinstance(assumpions[x][j], list)):
				col.append(assumpions[x][j])
		checkSets.append(col)
		quad = []
		i_quad = i / 3
		j_quad = j / 3

		for i1 in xrange(3 * i_quad, 3 * i_quad + 3):
			for j1 in xrange(3 * j_quad, 3 * j_quad + 3):
				if ((not (i1 == i and j1 == j) )and isinstance(assumpions[i1][j1], list)):
					quad.append(assumpions[i1][j1])
		checkSets.append(quad)

		for checkSet in checkSets:
			for targetNumber in target:
				isResult = True
				for assumpion in checkSet:
					if (targetNumber in assumpion):
						isResult = False
						break
				if (isResult):
					return targetNumber
	return None

def solvePuzzle(isPrinting, puzzle):
	if (getAsString(puzzle) in unsolvables):
		return []
	retval = copy.deepcopy(puzzle)
	for x in xrange(1,10000):
		solved = True
		madeProgress = False
		assumtions = [[0,0,0,0,0,0,0,0,0] for i in range(9)]

		for i in xrange(0, 9):
			for j in xrange(0, 9):
				assumtions[i][j] = puzzle[i][j]
				if (retval[i][j] == 0):
					solved = False
					assumtions[i][j] = getVariants(i, j, retval)
					if (len(assumtions[i][j]) == 0):
						unsolvables.add(getAsString(puzzle))
						return []
					if (len(assumtions[i][j]) == 1):
						retval[i][j] = assumtions[i][j][0]
						madeProgress = True
					else:
						solved = False
		if (solved):
			return retval
		if (not madeProgress):

			madeProgressAssumptions = False
			for i in xrange(0, 9):
				for j in xrange(0, 9):
					tmp = normalizeAssumption(i, j, assumtions)
					if (tmp):
						retval[i][j] = tmp
						madeProgressAssumptions = True

			if (madeProgressAssumptions):
				continue

			for assLen in xrange(2,10):
				for i in xrange(0, 9):
					for j in xrange(0, 9):
						if (isinstance(assumtions[i][j], list)):
							if (len(assumtions[i][j]) != assLen):
								continue
							assumpion = copy.deepcopy(retval)
							for k in assumtions[i][j]:
								assumpion[i][j] = k
								tmp = solvePuzzle(isPrinting - 1, assumpion)
								if len(tmp):
									return tmp
			unsolvables.add(getAsString(puzzle))
			return []
	return retval

answer = 0
ind = 0
for puzzle in puzzles:
	ind += 1
	 
	print "\npuzzle %d\n" % ind
	for x in puzzle:
		print x
	print "\nretval %d\n" % ind
	solved = solvePuzzle(1, puzzle)
	answer += solved[0][0] * 100 + solved[0][1] * 10 + solved[0][2]
	for x in solved:
		print x

print answer