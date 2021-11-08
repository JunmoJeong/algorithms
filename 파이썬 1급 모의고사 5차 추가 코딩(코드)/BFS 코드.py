#deque 사용
from collections import deque
result=[]
def bfs(graph, start, visited):
    q = deque([start])
    visited[start] = True
    while q:
        v = q.popleft()
        result.append(v)
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
    return result

graph = [
    [],
    [2, 3, 4],
    [1, 4],
    [6],
    [1, 2, 5],
    [4],
    [3]  ]
visited = [False] * 7
print(bfs(graph, 1, visited))

# 딕셔너리 사용
def bfs2(graph2, start_node):
    visited2 = list()
    q2 = list()
    q2.append(start_node)
    while q2:
        node = q2.pop(0)
        if node not in visited2:
            visited2.append(node)
            q2.extend(graph2[node])
    return visited2

graph2 = {
    '1': ['2','3','4'],
    '2': ['1','4'],
    '3': ['6'],
    '4': ['1','2','5'],
    '5': ['4'],
    '6': ['3'] }

print(bfs2(graph2, '1'))



