'''
미로탈출
홍길동 N x M 크기의 직사각형 형태의 미로. 미로에는 여러 마리의 괴물이 있다. 
홍길동 위치 (1,1)이고 미로의 출구는 (N,M)의 위치에 존재 한 번에 한 칸씩 이동
괴물이 있는 부분은 0, 괴물이 없는 부분은 1
미로는 반드시 탈출할 수 있는 형태로 제시
홍길동이 탈출하기 위해 움직여야 하는 최소 칸의 개수를 구하시오.(칸을 셀 때는 시작 칸과 마지막 칸을 모두 포함해서 계산)

입력조건
첫 째 줄에 두 정수 N,M 주어진다(4<=N, M<=200)
다음 N개의 줄에는 각각 M개의 정수(0 혹은 1)로 미로의 정보가 주어진다. 
시작칸과 마지막 칸은 항상 1이다. 

출력
첫째 줄에 최소 이동 칸의 개수를 출력
'''


'''
이 문제는 bfs를 이용했을 때 효과적으로 해결. bfs는 시작 지점에서 가까운 노드부터 차례대로 그래프의 모든 노드를 탐색하기 때문.
(1,1) 지점에서부터 bfs를 수행하여 모든 노드의 값을 거리 정보로 넣으면 된다. 
특정한 노드를 방문하면 그 이전 노드의 거리에 1을 더한 값을 리스트에 넣는다. 

'''


# N, M을 공백으로 구분하여 입력받기
from collections import deque
n, m = map(int, input().split())

# 2차원 리스트의 맵 정보 입력받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 이동할 네 방향 정의(상,하,좌,우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# bfs 구현


def bfs(x, y):
    # queue 구현을 위해 deque 라이브러리 사용
    queue = deque()
    queue.append((x, y))
    # 큐가 빌때까지 반복
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 네 방향으로 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 찾기 공간을 벗어난 경우 무시
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            # 괴물 만나는 경우
            if graph[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

    # 가장 오른쪽 아래까지의 최단 거리 반환
    return graph[n-1][m-1]


# bfs를 수행한 결과 출력
print(bfs(0, 0))
