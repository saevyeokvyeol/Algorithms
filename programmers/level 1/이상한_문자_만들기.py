def solution(s):
    answer = ""
    f = True
    
    for string in s:
        if string == " ":
            f = True
            answer += string
        elif f:
            f = False
            answer += string.upper()
        else:
            f = True
            answer += string.lower()
    return answer