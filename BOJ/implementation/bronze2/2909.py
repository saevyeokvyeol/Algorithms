c, k = map(int, input().split())
c += 0 if round(c, k * -1) != 0 else 1
print(round(c, k * -1))