num = {'-':0, '\\':1, '(':2, '@':3, '?':4, '>':5, '&':6, '%':7, '/':-1}
while True:
    string = input()
    if string == '#':
        break
    answer = 0
    string = string[::-1]
    for i in range(len(string)):
        answer += num[string[i]] * (8 ** i)
    print(answer)