# python3
import sys

def build_suffix_array(text):
	"""
	Build suffix array of the string text and
	return a list result of the same length as the text
	such that the value result[i] is the index (0-based)
	in text where the i-th lexicographically smallest
	suffix of text starts.
	"""
	result = []
	# Implement this function yourself
	my_hash = {}
	matrix = []
	for i in range(len(text)):
		matrix.append(text[i:] + text[:i])
		my_hash[matrix[-1]] = i
	matrix.sort()
	for each in matrix:
		result.append(my_hash[each])
	return result


if __name__ == '__main__':
	text = sys.stdin.readline().strip()
	print(" ".join(map(str, build_suffix_array(text))))
