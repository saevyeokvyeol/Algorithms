def solution(array, n):
    for i in range(100):
        if array.count(n - 1) >= 1:
            return n - i
        elif array.count(n + i) >= 1:
            return n + i