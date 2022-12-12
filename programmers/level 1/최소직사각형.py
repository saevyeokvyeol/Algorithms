def solution(sizes):
    x = y = 0
    for size in sizes:
        sx, sy = min(size), max(size)
        if x < sx: x = sx
        if y < sy: y = sy
    return x * y