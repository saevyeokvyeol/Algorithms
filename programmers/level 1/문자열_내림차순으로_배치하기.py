def solution(s):
    string = sorted(list(s), reverse=True)
    return ''.join(string)