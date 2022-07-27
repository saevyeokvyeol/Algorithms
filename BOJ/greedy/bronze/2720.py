import sys

money = [25, 10, 5, 1]

for _ in range(int(sys.stdin.readline())):
    C = int(sys.stdin.readline())

    result = []
    for i in money:
        result.append(C // i)
        C %= i
    print(*result)