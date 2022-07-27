import sys

# 풀이 1
B, C, D = map(int, sys.stdin.readline().split())
burger = sorted(list(map(int, sys.stdin.readline().split())), reverse=True)
side = sorted(list(map(int, sys.stdin.readline().split())), reverse=True)
drink = sorted(list(map(int, sys.stdin.readline().split())), reverse=True)

set = min(B, C, D)

price = (sum(burger[:set]) + sum(side[:set]) + sum(drink[:set])) * 0.9
price += sum(burger[set:]) + sum(side[set:]) + sum(drink[set:])

print(sum(burger) + sum(side) + sum(drink))
print(int(price))

# 풀이 2
count = list(map(int, sys.stdin.readline().split()))
N = len(count)
menu = [sorted(list(map(int, sys.stdin.readline().split()))) for _ in range(N)]

set = min(count)
price = 0

for i in range(N):
    for j in range(1, set + 1):
        price += menu[i][-j] * 0.9
        if j == set:
            price += sum(menu[i][:-set])

print(sum([sum(i) for i in menu]))
print(int(price))