T = int(input())

for _ in range(T):
    N = input()
    num = str(int(N) + int(N[::-1]))
    n_len = len(N) // 2
    answer = "YES"
    
    for i in range(n_len):
        if num[i] != num[-1 - i]:
            answer = "NO"
            break
        
    print(answer)