def solution(S):
    left = 0
    for s in S:
        if s == "(":
            left += 1
        else:
            left -= 1
        if left < 0:
            return False
    return True if left == 0 else False