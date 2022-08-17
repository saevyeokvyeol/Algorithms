import sys

while True:
    T = list(map(int, sys.stdin.readline().split()))
    if sum(T) == 0:
        break
    print("Yes") if T[0] > T[1] else print("No")