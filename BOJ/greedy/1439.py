# 풀이 1
S = input()
result = 0
num = 2

for s in S:
    if num != s:
        result += 1
        num = s

print(result // 2)

# 풀이 2
from math import ceil

S = input()
result = S.count("01")
result += S.count("10")
print(ceil(result / 2))