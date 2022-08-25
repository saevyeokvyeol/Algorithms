# 풀이 1
while True:
    s = input()
    if s == "END":
        break
    s = reversed(list(s))
    print(*s, sep="")

# 풀이 2
while True:
    s = input()
    if s == "END":
        break
    print(s[::-1])