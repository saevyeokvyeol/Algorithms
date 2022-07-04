import sys

word = sorted(list(sys.stdin.readline().rstrip().upper()))
result = sorted(set(word))

# for r in result:
#   result[0]word.count(r)