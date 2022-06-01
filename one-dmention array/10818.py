import sys

T = int(sys.stdin.readline())
N = sorted(list(map(int, sys.stdin.readline().split())))

print(N[0], N[T - 1])