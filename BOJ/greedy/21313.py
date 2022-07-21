oc = int(input())

result = [i % 2 + 1 for i in range(oc)]
if oc % 2 != 0:
    result[-1] = 3

print(*result)