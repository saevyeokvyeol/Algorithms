def solution(s):
    s = s.split()
    for i in range(len(s)):
        if s[i] == "Z":
            del s[i - 1:i + 1]
    return sum(map(int, s))