# python3
import sys

NA = -1

class Node:
	def __init__ (self):
		self.next = [NA] * 4

def solve (text, n, patterns):
    result = []
    trie = build_trie(patterns)
    for i in range(0, len(text)):
        current_node = 0
        j = i
        while j < len(text) and text[j] in trie[current_node]:
            current_node = trie[current_node][text[j]]
            if '$' in trie[current_node]:
                result.append(i)
                break
            j += 1
    return result


def build_trie(patterns):
    root = 0
    count = 1
    tree = dict()
    for pattern in patterns:
        current_node = root
        for each in pattern:
            if current_node not in tree:
                tree[current_node] = {}
            if each not in tree[current_node]:
                tree[current_node][each] = count
                count += 1
            current_node = tree[current_node][each]
        tree[current_node] = {'$': count}
        count += 1
    # write your code here
    return tree


text = sys.stdin.readline ().strip ()
n = int (sys.stdin.readline ().strip ())
patterns = []
for i in range (n):
	patterns += [sys.stdin.readline ().strip ()]

ans = solve (text, n, patterns)

sys.stdout.write (' '.join (map (str, ans)) + '\n')
