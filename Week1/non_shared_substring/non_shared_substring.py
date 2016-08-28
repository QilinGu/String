# python3
import sys

count = 1

def add_to_trie(trie, word, node, to_node):
    if node in trie:
        trie[node][word] = to_node
    else:
        trie[node] = {word: to_node}


def move_on_the_trie(trie, word, node):
    if not word:
        return
    global count
    needed_word = None
    word_to_add = None
    rest_of_the_word = None
    for each in trie[node].keys():
        j = 0
        while j < len(word) and j < len(each) and each[j] == word[j] :
            j += 1
        if j != 0:
            needed_word = each
            word_to_add = word[:j]
            rest_of_the_word = word[j:]
    if needed_word:
        if needed_word == word_to_add:
            node = trie[node][word_to_add]
        else:
            add_to_trie(trie, word_to_add, node, count)
            count += 1
            add_to_trie(trie, needed_word[len(word_to_add):], trie[node][word_to_add], trie[node][needed_word])
            del trie[node][needed_word]
            node = trie[node][word_to_add]

        move_on_the_trie(trie, rest_of_the_word, node)
    else:
        add_to_trie(trie, word, node, count)
        count += 1
    return


def build_suffix_tree(text):
    result = []
    trie = {}
    for i in range(len(text)):
        word = text[i:]
        current_node = 0
        if current_node not in trie:
            trie[current_node] = {}
        move_on_the_trie(trie, word, current_node)
    return trie


def solve(p, q):
    trie = build_suffix_tree("%s#%s$" % (p, q))
    print(trie)
    word = 'ATG'
    state = 0
    for each in word:
        print(state, trie[state])
        state = trie[state][each]
    print(state, trie[state])
    return ''

p = sys.stdin.readline ().strip ()
q = sys.stdin.readline ().strip ()

ans = solve (p, q)

sys.stdout.write (ans + '\n')

