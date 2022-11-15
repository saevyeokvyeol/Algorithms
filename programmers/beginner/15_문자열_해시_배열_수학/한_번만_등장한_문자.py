def solution(s):
    answer = [chr(i) for i in range(97, 97 + 26) if s.count(chr(i)) == 1]
    return ''.join(answer)