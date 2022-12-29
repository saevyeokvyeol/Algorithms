def solution(s):
    zero = cnt = 0
    while s != "1":
        zero += s.count("0")
        s = bin(len(s.replace("0", "")))[2:]
        print(s)
        cnt += 1
    return [cnt, zero]