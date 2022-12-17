def solution(string, n):
    answer = ''
    for s in string:
        if s == ' ':
            answer += ' '
            continue
        new_s = chr(ord(s) + n)
        if (s.isupper() and new_s > 'Z') or new_s > 'z':
            new_s = chr(ord(new_s) - 26) 
        answer += new_s
    return answer