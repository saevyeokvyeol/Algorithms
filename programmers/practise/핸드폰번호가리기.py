def solution(phone_number):
    answer = phone_number.replace(phone_number[:-4], '*' * (len(phone_number) - 4))
    return answer

print(solution("01033334444"))
print(solution("027778888"))