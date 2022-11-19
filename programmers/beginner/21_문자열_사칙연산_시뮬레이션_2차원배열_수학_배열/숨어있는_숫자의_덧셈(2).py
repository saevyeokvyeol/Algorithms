def solution(my_string):
    answer = 0
    num = '0'
    for s in my_string:
        if s.isdigit():
            num += s
        else:
            answer += int(num)
            num = '0'
    answer += int(num)
    return answer