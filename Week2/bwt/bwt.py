# python3
import sys

def BWT(text):
    matrix = []
    for i in range(len(text)):
        matrix.append(text[i:] + text[:i])
    matrix.sort()
    print(matrix)
    result = ''
    for each in matrix:
        result += each[-1]
    return result

if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    print(BWT(text))