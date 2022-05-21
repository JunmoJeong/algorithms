from collections import deque
INF = 1e9  # 무한을 의미하는 값으로 10억 설정

# 맵의 크기 N을 입력 받기
n = int(input())

# 전체 모든 칸에 대한 정보 입력
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 아기 상어의 현재 크기 변수와 현재 위치 변수
now_size = 2
now_x, now_y = 0, 0

# 아기 상어의 시작 위치를 찾은 뒤에 그 위치엔 아무것도 없다고 처리
for i in range(n):
    for j in range(n):
        if array[i][j] == 9:
            now_x, now_y = i, j
            array[now_x][now_y] = 0

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 모든 위치까지의 '최단 거리'만 계산하는 BFS 함수


def bfs():
    # 값이 -1이라면 도달할 수 없다는 의미(초기화)
    dist = [[-1] * n for _ in range(n)]
    # 시작 위치는 도달이 가능하다고 보며 거리는 0
    q = deque([(now_x, now_y)])
    dist[now_x][now_y] = 0
