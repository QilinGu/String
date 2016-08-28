# python3
import sys


def InverseBWT(bwt):
    my_hash = {
        '$': 0,
        'A': 0,
        'C': 0,
        'G': 0,
        'T': 0
    }
    last_column_hash = {}
    last_column = []
    for i,each in enumerate(bwt):
        last_column_hash[(each, my_hash[each])] = i
        last_column.append((each, my_hash[each]))
        my_hash[each] += 1
    first_column = sorted(last_column)
    result = ''
    index = last_column_hash[('$', 0)]
    while len(result) != len(bwt):
        letter_and_position = first_column[index]
        result += letter_and_position[0]
        index = last_column_hash[letter_and_position]
    return result

if __name__ == '__main__':
    bwt = sys.stdin.readline().strip()
    print(InverseBWT(bwt))