# 풀이 1 (오답)
# a, k = map(int, input().split())
# result = 0

# while a * 2 <= k:
#     a *= 2
#     result += 1
# while a != k:
#     a += 1
#     result += 1
# print(result)

# 풀이 2 (시뮬레이션)
a, k = map(int, input().split())
result = 0
while k > a:
    while k % 2 == 0 and k // 2 >= a:
        k //= 2
        result += 1
    if k > a:
        k -= 1
        result += 1
print(result)