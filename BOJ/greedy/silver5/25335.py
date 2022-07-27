import sys

N, M = map(int, sys.stdin.readline().split())
dot = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
line = [sys.stdin.readline().split()[2] for _ in range(M)]

R = line.count('R')
G = line.count('G')
B = line.count('B')
if R > B:
    print('jhnah917')
elif B > R:
    print('jhnan917')
else:
    if M % 2 == 0:
        print('jhnan917')
    else:
        print('jhnah917')