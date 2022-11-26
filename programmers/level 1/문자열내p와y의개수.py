def solution(s):
    s = list(s.lower())
    if s.count('p') == s.count('y'):
        return True
    else:
        return False