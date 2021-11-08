#dfs 깊이우선탐색

#1. 재귀 호출 사용
result=[]

def dfs(graph, v,visited):
    visited[v]=True
    result.append(v)
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)
    return result

graph = [
    [],
    [2,3,4],
    [1,4],
    [6],
    [1,2,5],
    [4],
    [3]  ]

visited=[False]*7
print(dfs(graph, 1,visited))



#2. 딕셔너리 사용 
def dfs2(graph, start):
    visited2 = list()
    stack = list()
    stack.append(start)

    while stack:
        node = stack.pop()
        if node not in visited2:
            visited2.append(node)
            stack.extend(reversed(graph[node]))
    return visited2

graph = {
    '1': ['2','3','4'],
    '2': ['1','4'],
    '3': ['6'],
    '4': ['1','2','5'],
    '5': ['4'],
    '6': ['3'] }

print(dfs2(graph, '1'))



