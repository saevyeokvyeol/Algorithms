def solution(brown, yellow):
    total = brown + yellow
    for i in range(1, int(total ** 0.5) + 1):
        x = total // i
        y = i
        if (x - 2) * (y - 2) == yellow:
            return [x, y]