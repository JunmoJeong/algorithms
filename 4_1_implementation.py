'''
N x N 크기의 정사각형 공간위에 여행가 A가 있다
여행가 A는 상,하,좌,우 방향으로 이동 가능 시작 좌표는 항상 1,1
N x N 크기 공간을 벗어나는 움직임은 무시
계획서 주어졌을 때 여행가 A 최종 좌표구하기

입력
5 
R R R U D D
출력
3 4

이동 횟수가 N번이면 시간 복잡도도 O(N)이다.

'''
# N을 입력받기

n = int(input())
x, y = 1,1
plans = input().spllit()

# L, R, U, D에 따른 이동 방향
dx = [0,0,-1,1]
dy = [-1,1,0,0]

move_types = ['L','R','U','D']

# 이동 계획을 하나씩 확인
for plan in plans:
    # 이동 후 좌표 구하기
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]

    # 공간을 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    # 이동 수행
    x, y = nx, ny
print(x,y)


### 수정 
