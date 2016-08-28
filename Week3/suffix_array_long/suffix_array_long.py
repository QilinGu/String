# python3
import sys


def sort_characters(text):
	order = [None for i in range(len(text))]
	alpha = len(set(text))
	my_hash = {}
	for i, each in enumerate(sorted(set(text))):
		my_hash[each] = i
	count = [0 for i in range(alpha)]
	for i in range(0, len(text)):
		count[my_hash[text[i]]] += 1
	for j in range(1, alpha):
		count[j] += count[j - 1]
	i = len(text) - 1
	while i >= 0:
		c = my_hash[text[i]]
		count[c] -= 1
		order[count[c]] = i
		i -= 1
	return order


def compute_char_classes(text, order):
	clas = [None for _ in range(len(text))]
	clas[order[0]] = 0
	for i in range(1, len(text)):
		clas[order[i]] = clas[order[i - 1]]
		if text[order[i]] != text[order[i-1]]:
			clas[order[i]] += 1
	return clas


def sort_doubled(text, L, order, clas):
	count = [0 for i in range(len(text))]
	newOrder = [None for i in range(len(text))]
	for i in range(len(text)):
		count[clas[i]] += 1
	for j in range(1, len(text)):
		count[j] += count[j - 1]
	i = len(text) - 1
	while i >= 0:
		start = (order[i] - L + len(text)) % len(text)
		cl = clas[start]
		count[cl] -= 1
		newOrder[count[cl]] = start
		i -= 1
	return newOrder


def updated_classes(order, clas, L):
	n = len(order)
	new_class = [None for i in range(n)]
	new_class[order[0]] = 0
	for i in range(1, n):
		cur = order[i]
		prev = order[i - 1]
		mid = (cur + L) % n
		mid_prev = (prev + L) % n
		new_class[cur] = new_class[prev]
		if clas[cur] != clas[prev] or clas[mid] != clas[mid_prev]:
			new_class[cur] += 1
	return new_class


def lcp_of_suffixes(text, i, j, equal):
	print(equal, text[i:], text[j:])
	lcp = equal
	while i + lcp < len(text) and j + lcp < len(text):
		if text[i + lcp] == text[j + lcp]:
		    lcp += 1
		else:
		    break
	return lcp


def invert_suffix_array(order):
    pos = [None for _ in range(len(order))]
    for i in range(len(pos)):
        pos[order[i]] = i
    return pos


def compute_lcp_array(text, order):
    lcp_array = [None for i in range(len(text) - 1)]
    lcp = 0
    pos_in_order = invert_suffix_array(order)
    suffix = order[0]
    for i in range(len(text)):
        order_index = pos_in_order[suffix]
        if order_index == len(text) - 1:
            lcp = 0
            suffix = (suffix + 1) % len(text)
            continue
        next_suffix = order[order_index + 1]
        if lcp > 0:
	        lcp = lcp_of_suffixes(text, suffix, next_suffix, lcp - 1)
        else:
	        lcp = lcp_of_suffixes(text, suffix, next_suffix, 0)
        lcp_array[order_index] = lcp
        suffix = (suffix + 1) % len(text)
    return lcp_array


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
	order = sort_characters(text)
	clas = compute_char_classes(text, order)
	L = 1
	while L < len(text):
		order = sort_doubled(text, L, order, clas)
		clas = updated_classes(order, clas, L)
		L *= 2
	result = order
	print(compute_lcp_array(text, result))
	for each in result:
		print(text[each:])
	return result


if __name__ == '__main__':
	text = sys.stdin.readline().strip()
	print(" ".join(map(str, build_suffix_array(text))))
