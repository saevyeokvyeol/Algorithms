def solution(sides):
    sides.sort()
    if sum(sides[:2]) > sides[2]:
        return 1
    else:
        return 2