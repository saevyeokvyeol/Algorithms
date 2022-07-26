R, G, B = map(int, input().split())
result = (R // 3) + (G // 3) + (B // 3)
R, G, B = R % 3, G % 3, B % 3
if [R, B, G].count(0) == 2:
    result += 1
else:
    result += max(R, B, G)
print(result)