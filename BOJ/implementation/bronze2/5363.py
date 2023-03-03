for _ in range(int(input())):
    S = input().split()
    print(*(S[2:] + S[:2]))