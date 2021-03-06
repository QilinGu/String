# python3
import sys

def prefix_array(string):
  s = [0]
  border = 0
  for i in range(1, len(string)):
    while border > 0 and string[i] != string[border]:
      border = s[border - 1]
    if string[i] == string[border]:
      border += 1
    else:
      border = 0
    s.append(border)
  return s

def find_pattern(pattern, text):
  """
  Find all the occurrences of the pattern in the text
  and return a list of all positions in the text
  where the pattern starts in the text.
  """
  result = []
  # Implement this function yourself
  s = prefix_array(pattern + '$' + text)
  for i, each in enumerate(s):
    if each == len(pattern):
      result.append(i - 2 * len(pattern))
  return result


if __name__ == '__main__':
  pattern = sys.stdin.readline().strip()
  text = sys.stdin.readline().strip()
  result = find_pattern(pattern, text)
  print(" ".join(map(str, result)))

