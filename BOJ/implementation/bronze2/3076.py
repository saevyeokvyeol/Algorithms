R, C = map(int, input().split())
A, B = map(int, input().split())

for r in range(R):
    for a in range(A):
        for c in range(C):
                if c % 2 == r % 2:
                    print('X' * B, end="")
                else:
                    print('.' * B, end="")
        print()