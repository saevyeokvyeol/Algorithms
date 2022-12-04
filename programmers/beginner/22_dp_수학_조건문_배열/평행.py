def solution(dots):
    lines = []
    for i in range(len(dots)):
        for j in range(i + 1, len(dots)):
            x1, y1 = dots[i]
            x2, y2 = dots[j]
            lines.append((x1 - x2) / (y1 - y2))
    return 0 if len(set(lines)) == len(lines) else 1