N = int(input())
store = list(map(int, input().split()))
count = 0
uyu = [0, 1, 2]

for i in range(len(store)):
    if uyu[count % 3] == store[i]:
        count += 1

print(count)