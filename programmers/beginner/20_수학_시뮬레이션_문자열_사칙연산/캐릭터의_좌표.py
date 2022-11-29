# 첫 번째 풀이
def solution(keyinput, board):
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    direction = ['left', 'down', 'right', 'up']
    margin = [b // 2 for b in board]
    answer = [0] * 2
    for i in keyinput:
        d = direction.index(i)
        answer[0] += dx[d]
        answer[1] += dy[d]
        if answer[0] < margin[0] * -1: answer[0] = margin[0] * -1
        elif answer[0] > margin[0]: answer[0] = margin[0]
        elif answer[1] < margin[1] * -1: answer[1] = margin[1] * -1
        elif answer[1] > margin[1]: answer[1] = margin[1]
    return answer

# 두 번째 풀이
def solution(keyinput, board):
    direction = {'left' : (-1, 0), 'down' : (0, -1), 'right' : (1, 0), 'up' : (0, 1)}
    margin = [b // 2 for b in board]
    answer = [0] * 2
    
    for i in keyinput:
        x, y = direction[i]
        
        if abs(answer[0] + x) > margin[0] or abs(answer[1] + y) > margin[1]:
            continue
        else:
            answer[0] += x
            answer[1] += y
    return answer

print(solution(["left", "right", "up", "right", "right"], [11, 11]))