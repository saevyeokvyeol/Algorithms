# 첫 번째 풀이
def solution(dots):
    dots.sort()
    height = abs(max(dots[0][0], dots[3][0]) - min(dots[0][0], dots[3][0]))
    weight = abs(max(dots[0][1], dots[3][1]) - min(dots[0][1], dots[3][1]))
    answer = height * weight
    return answer

# 두 번째 풀이
def solution(dots):
    height = max(dots)[0] - min(dots)[0]
    weight = max(dots)[1] - min(dots)[1]
    answer = height * weight
    return answer