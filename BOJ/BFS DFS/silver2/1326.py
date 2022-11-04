# 풀이 1(오답)
n = int(input())
bridge = list(map(int, input().split()))
a, b = map(int, input().split())
result = [False] * (n + 1)

def dfs(map, start, end):
    result[start] = True
    if (end - start) % map[start - 1] == 0:
        print(result.count(True))
    else:
        dfs(map, start + 1, end)
    
dfs(bridge, a, b)

# 풀이 2
from collections import deque
n = int(input())
bridge = list(map(int, input().split()))
a, b = map(int, input().split())
result = [-1] * (n + 1)

def bfs(start, end, bridge, n, result):
    queue = deque([start])
    result[start] = 0
    while queue:
        v = queue.popleft()
        for i in range(v, n + 1, bridge[v - 1]):
            if result[i] == -1:
                queue.append(i)
                result[i] = result[v] + 1
                if i == end:
                    return result[i]
        for i in range(v, 0, -bridge[v - 1]):
            if result[i] == -1:
                queue.append(i)
                result[i] = result[v] + 1
                if i == end:
                    return result[i]
    return -1

print(bfs(a, b, bridge, n, result))