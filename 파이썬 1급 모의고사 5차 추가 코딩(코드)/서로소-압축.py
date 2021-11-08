def find(parent, value):
    if value == parent[value]:
        return value
    parent[value]=find(parent, parent[value])
    return parent[value]

def union(parent, u, v):
    u = find(parent, u)
    v = find(parent, v)
    parent[u]=v
    return parent

def solution(n, connections):
    parent = [i for i in range(n+1)]
    for i, connection in enumerate(connections):
        parent= union(parent, connection[0], connection[1])

    #각 원소의 부모에 들어간 값
    print("각 원소의 대표(부모)값:", parent)
    
    # 각 원소의 진짜 부모 - 속한 집합 확인
    print("각 원소가 속한 집합 확인하기:", end='')
    for i in range(1,n+1):
        print(find(parent,i), end=' ')


#아래는 테스트케이스 출력을 해보기 위한 코드입니다.


n = 5
connections = [[1,2],[1,3],[1,4],[4,5],[1,5]]
solution(n, connections)
print()
n = 6
connections = [[1,2],[3,6],[3,4],[1,4]]
solution(n, connections)
