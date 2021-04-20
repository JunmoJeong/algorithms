'''
게임 개발
캐릭터가 있는 장소는 N x M 크기의 직사각형 각각의 칸은 육지 또는 바다
캐릭터는 동서남북 중 한 곳을 바라본다
각 칸은 (A,B)로 표현 A는 북쪽으로부터 떨어진 칸의 개수
B는 서쪽으로부터 떨어진 칸의 개수
캐릭터는 상하좌우로 움직일 수 있고 바다로 되어 있는 공간에는 갈 수 없다

캐릭터 움직임 메뉴얼
1. 현재 위치에서 현재 방향을 기준으로 왼쪽방향부터 차례대로 갈 곳을 정함
2. 캐릭터의 바로 왼쪽 방향에 아직 가보지 않은 칸이 존재한다면 왼쪽 방향으로 회전한 다음
왼쪽으로 한 칸을 전진한다. 왼쪽 방향에 가보지 않은 칸이 없다면 왼쪽 방향으로 회전만 
수행하고 1단계로 돌아간다. 
3. 만약 네 방향 모두 이미 가본 칸이거나 바다로 되어 있는 칸인 경우에는 바라보는 방향을
유지한 채로 한 칸 뒤로 가고 1단계로 돌아간다. 뒤쪽 방향이 바다인 칸이라 뒤로갈 수 없는
경우에는 움직임을 멈춘다. 

캐릭터가 방문한 칸의 수를 출력하는 프로그램
입력 조건
- 첫째 줄에 맵의 세로 크기 N과 가로 크기 M을 공백으로 구분하여 입력
- 둘째 줄에 캐릭터가 있는 칸의 좌표 (A,B)와 바라보는 방향 d가 서로 공백으로 구분하여 주어짐
- 셋째 줄부터 맵이 육지인지 바다인지 입력. N개의 줄에 맵의 상태가 북쪽부터 남쪽 순서대로
각줄의 데이터는 서쪽부터 동쪽 순서대로 주어진다. 맵의 외곽은 항상 바다로 되어 있다. 
- 처음 캐릭터가 위치한 칸의 상태는 항상 육지이다.

입력 
4 4
1 1 0
1 1 1 1 
1 0 0 1
1 1 0 1
1 1 1 1

출력 3

'''
# N, M을 공백으로 구분하여 입력받기
n, m = map(int, input().split())

# 맵을 생성하여 0으로 초기화
d = [[0] * m for _ in range(n)]

# 현재 캐릭터의 X 좌표, Y 좌표, 방향을 입력받기
x, y, direction = map(int, input().split())

# 현재 좌표 방문처리
d[x][y] = 1 

# 전체 맵 정보를 받기
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 북, 동, 남, 서 방향 정의
dx = [-1,0,1,0]
dy = [0,1,0,-1]

# 왼쪽으로 회전
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

# 시뮬레이션 시작
count = 1
turn_time = 0

while True:
    # 왼쪽으로 회전
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
    if d[nx][ny] == 0 and array[nx][ny] ==0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
    else:
        turn_time += 1
    # 네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]

        # 뒤로 갈 수 있다면 이동하기
        if array[nx][ny] == 0:
            x = nx
            y = ny
        # 뒤가 바다로 막혀있는 경우
        else:
            break
        turn_time  = 0

print(count)
