def solution(my_string):
    answer = ''
    for i in range(len(my_string)):
        if my_string[:i].count(my_string[i]) == 0:
            answer += my_string[i]
    return answer