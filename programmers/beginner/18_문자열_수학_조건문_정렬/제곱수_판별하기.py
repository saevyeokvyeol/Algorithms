# 첫 번째 풀이
def solution(n):
    return 1 if (n ** 0.5) % 1 == 0 else 2

# 두 번째 풀이
def solution(n):
    return 1 if (n ** 0.5).is_integer() else 2