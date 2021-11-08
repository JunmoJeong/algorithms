def solution(n, garden):
    answer = 0
    dx = [ -1, 1, 0, 0 ]
    dy = [ 0, 0, -1, 1 ]
    day=1
    answer=0
    is_full=False
    while not is_full:
        is_full=True
        for x in range(0,n):
            for y in range(0,n):
                if garden[x][y] ==day:
                    for d in range(0,4):
                        nx=x+dx[d]
                        ny=y+dy[d]
                        if 0<=nx<n and 0<=ny<n and  garden[nx][ny]==0 :
                            is_full =False
                            garden[nx][ny]=day+1
                            answer=day
        day+=1
    return answer


#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
n1 = 3
garden1 = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
ret1 = solution(n1, garden1)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

n2 = 2
garden2 = [[1, 1], [1, 1]]
ret2 = solution(n2, garden2)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")
