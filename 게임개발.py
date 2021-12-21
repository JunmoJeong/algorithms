# N, M 을 공백으로 구분하여 입력받기
n, m = map(int, input().split(' '))

# 방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
d = [[0]*m for _ in range(n)]
print(d)
