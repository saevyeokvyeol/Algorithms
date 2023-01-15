for _ in range(int(input())):
    A, N = input().split('-')
    an = 0
    for i in range(3):
        an += (ord(A[i]) - 65) * 26 ** (2 - i)
    print("nice" if abs(an - int(N)) <= 100 else "not nice")