def solution(n):
    count = 1
    for i in range(1, 12):
        count *= i
        if count > n:
            return i - 1