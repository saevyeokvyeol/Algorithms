score = {'A':4, 'B':3, 'C':2, 'D':1,'F':0.0}
pm = {'+':0.3, '0':0.0, '-':-0.3}
S = list(input())

result = score.get(S[0])

if len(S) == 2:
    result += pm.get(S[1])

print(result)