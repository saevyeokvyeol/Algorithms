def solution(babbling):
    ong_al_i = ["aya", "ye", "woo", "ma"]
    answer = 0
    for b in babbling:
        for o in ong_al_i:
            b.replace(o, "")
        if len(b) == 0:
            answer += 1
    return answer