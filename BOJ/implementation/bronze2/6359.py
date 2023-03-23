# 첫 번째 풀이
# for _ in range(int(input())):
#     n = int(input())
#     room = [False] * (n + 1)
#     for i in range(1, n + 1):
#         for j in range(i, n + 1, i):
#             room[j] = not room[j]
#     print(room.count(True))

# 두 번째 풀이
for _ in range(int(input())):
    n = int(input())
    result = 0
    for i in range(1, n + 1):
        if i ** 0.5 == int(i ** 0.5):
            result += 1
    print(result)