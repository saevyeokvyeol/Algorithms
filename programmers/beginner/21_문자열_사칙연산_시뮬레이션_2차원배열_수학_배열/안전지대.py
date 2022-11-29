def solution(board):
    length = len(board)
    answer = [[0] * length for _ in range(length)]
    danger = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]
    for i in range(length):
        for j in range(length):
            if board[i][j] == 1:
                for d in danger:
                    x, y = d
                    if 0 <= (i + x) < length and 0 <= (j + y) < length:
                        answer[i + x][j + y] = 1
    return sum([a.count(0) for a in answer])