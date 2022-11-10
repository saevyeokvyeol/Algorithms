def solution(slice, n):
    for i in range(100):
        if slice * i // n >= 1:
            return i