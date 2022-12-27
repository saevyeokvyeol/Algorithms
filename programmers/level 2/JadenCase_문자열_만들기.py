def solution(s):
    answer = ""
    flag = None
    for i in s:
        if '0' <= i <= '9' or i == " ":
            answer += i
        elif flag == None or flag == " ":
            answer += i.upper()
        else:
            answer += i.lower()
        flag = i
    return answer