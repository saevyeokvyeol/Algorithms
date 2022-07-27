import sys

def apple_game(M, N, J, apple):
    result = 0
    W = 1

    for i in range(0, J):
        if W >= apple[i]:
            result += W - apple[i]
            W = apple[i]
        else:
            if apple[i] > W + (N - 1):
                result += apple[i] - W - (N - 1)
                W = apple[i] - (N - 1)
    print(result)

M, N = map(int, sys.stdin.readline().split())
J = int(sys.stdin.readline())
apple = [int(sys.stdin.readline()) for _ in range(J)]
apple_game(M, N, J, apple)

M = 5
N = 1
J = 3
apple = [1, 5, 3]
apple_game(M, N, J, apple)

M = 5
N = 2
J = 3
apple = [1, 5, 3]
apple_game(M, N, J, apple)