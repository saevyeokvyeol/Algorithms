# 풀이 1
string = input()
result = "I hate UCPC"

ucpc = ''
for i in string:
    if len(ucpc) == 0 and i == 'U':
        ucpc += i
    elif len(ucpc) == 1 and i == 'C':
        ucpc += i
    elif len(ucpc) == 2 and i == 'P':
        ucpc += i
    elif len(ucpc) == 3 and i == 'C':
        ucpc += i

if ucpc == "UCPC":
    print(result.replace("hate", "love"))
else:
    print(result)

# 풀이 2
ucpc = 'UCPC'
cnt = 0

for i in input():
    if i == ucpc[cnt]:
        cnt += 1
        if cnt == 4:
            break

if cnt == 4:
    print("I love UCPC")
else:
    print("I hate UCPC")