n = int(input())
x = list(map(int, input().split()))
sum = 0

for i in range(len(x)):
    for j in range(len(x)):
        sum += abs(x[i] - x[j])

print(sum)