import sys

# 풀이 1
num = int(sys.stdin.readline())
string = sys.stdin.readline()
print(string.count('pPAp'))

# 풀이 2
num = int(input())
string = input()
ppap = ['p', 'P', 'A']
result = cnt = 0

for s in string:
    if s == ppap[cnt % 3]:
        if cnt == 3:
            cnt = 0
            result += 1
        else:
            cnt += 1
    elif s == 'p':
        cnt = 1
    else:
        cnt = 0

print(result)

# 풀이 3
num = int(sys.stdin.readline())
string = sys.stdin.readline().rstrip()
string = string.replace('pPAp', '')
print((num - len(string)) // 4)