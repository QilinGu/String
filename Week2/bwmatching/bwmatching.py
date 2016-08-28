# python3
import sys
from Week2.bwtinverse.bwtinverse import *




def preprocess_bwt(bwt):
	first_column = sorted(bwt)
	starts = {}
	occ_counts_before = {}
	for i, each in enumerate(first_column):
		if each not in starts:
			starts[each] = i
			occ_counts_before[each] = []
	for each in bwt:
		for key in occ_counts_before.keys():
			if occ_counts_before[key]:
				to_add = occ_counts_before[key][-1]
			else:
				to_add = 0
			if each == key:
				to_add += 1
			occ_counts_before[key].append(to_add)
	return starts, occ_counts_before


def count_occurrences(pattern, bwt, starts, occ_counts_before):
	"""
	Compute the number of occurrences of string pattern in the text
	given only Burrows-Wheeler Transform bwt of the text and additional
	information we get from the preprocessing stage - starts and occ_counts_before.
	"""
	# Implement this function yourself
	top = 0
	bottom = len(bwt) - 1
	pattern = list(pattern)
	while top <= bottom:
		if pattern:
			symbol = pattern.pop(-1)
			if occ_counts_before[symbol][bottom] > occ_counts_before[symbol][top]:
				top = starts[symbol] + occ_counts_before[symbol][top] - 1
				bottom = starts[symbol] + occ_counts_before[symbol][bottom] - 1
			else:
				return 0
			print(top, bottom, symbol)
		else:
			return bottom - top + 1
	return 0



if __name__ == '__main__':
	bwt = sys.stdin.readline().strip()
	pattern_count = int(sys.stdin.readline().strip())
	patterns = sys.stdin.readline().strip().split()
	# Preprocess the BWT once to get starts and occ_count_before.
	# For each pattern, we will then use these precomputed values and
	# spend only O(|pattern|) to find all occurrences of the pattern
	# in the text instead of O(|pattern| + |text|).
	starts, occ_counts_before = preprocess_bwt(bwt)
	print(InverseBWT(bwt))
	print(starts)
	print(occ_counts_before, '\n')
	occurrence_counts = []
	first_column = sorted(bwt)
	for i in range(len(bwt)):
		print(i, first_column[i], bwt[i])
	print('')
	for pattern in patterns:
		occurrence_counts.append(count_occurrences(pattern, bwt, starts, occ_counts_before))
		print('')
	print(' '.join(map(str, occurrence_counts)))
