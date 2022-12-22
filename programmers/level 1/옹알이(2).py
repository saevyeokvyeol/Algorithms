def solution(babbling):
    sound = ["aya", "ye", "woo", "ma"]
    answer = 0
    for b in babbling:
        for s in sound:
            if s * 2 in b:
                continue
            b = b.replace(s, " ")
        if b.strip() == "":
            answer += 1
    return answer