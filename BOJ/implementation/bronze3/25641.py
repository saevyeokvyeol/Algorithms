n = int(input())
stst = input()
for i in range(n):
    if stst[i:].count('s') == stst[i:].count('t'):
        print(stst[i:])
        break