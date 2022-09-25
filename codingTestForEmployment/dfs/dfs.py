# DFS 함수 정의
def dfs(gragh, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end=" ")
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in gragh[v]:
        if not visited[i]:
            dfs(gragh, i, visited)
        
# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
gragh = [
    [],
    [2, 3],
    [1, 4, 5],
    [1, 6, 7],
    [2, 8],
    [2],
    [3, 7],
    [3, 6],
    [4]
]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현
visited = [False] * 9

# 정의된 DFS 함수 호출
dfs(gragh, 1, visited)