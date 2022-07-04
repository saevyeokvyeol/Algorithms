def solution(s):
    s = list(s.lower().split(" "))
    answer = ""

    for i in range(len(s)):
        for j in range(len(s[i])):
            if j % 2 == 0:
                s[i] = s[i].replace(s[i][j:j + 1], s[i][j:j + 1].upper(), 1)
        if i > 0:
            answer += " "
        if s[i] != " ":
            answer += s[i]
    return answer

print(solution("try hello world"))