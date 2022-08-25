s = list(input())
print(*[s.count(chr(i)) for i in range(97, 97 + 26)])