def solution(rsp):
    gbb = ["5", "2", "0"]
    answer = [gbb[(gbb.index(i) + 1) % 3] for i in rsp]
    return "".join(answer)