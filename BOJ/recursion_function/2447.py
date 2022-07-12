# 1차
# def star(N):
#     if N == 1:
#         return ['*']
#     else:
#         lst = [[" "] * 3 for _ in range(3)]
#         for i in range(3):
#             for j in range(3):
#                 if i == j == 1:
#                     lst[i][j] = space(N // 3)
#                 else:
#                     lst[i][j] = star(N // 3)

#         return lst

# def space(N):
#     if N == 1:
#         return [' ']
#     else:
#         lst = [[" "] * 3 for _ in range(3)]
#         for i in range(3):
#             for j in range(3):
#                 lst[i][j] = space(N // 3)

#         return lst

# n = int(input())
# print(*star(n), sep="\n")

# 2차
def star(N):
    if N == 1:
        return '*'
    
    stars = star(N // 3)
    lst = []

    for S in stars:
        lst.append(S * 3)
    for S in stars:
        lst.append(S + " " * (N // 3) + S)
    for S in stars:
        lst.append(S * 3)
    return lst

n = int(input())
print(*star(n), sep="\n")