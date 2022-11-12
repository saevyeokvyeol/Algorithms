def solution(age):
    answer = [str(chr(int(i) + 97)) for i in str(age)]
    return "".join(answer)