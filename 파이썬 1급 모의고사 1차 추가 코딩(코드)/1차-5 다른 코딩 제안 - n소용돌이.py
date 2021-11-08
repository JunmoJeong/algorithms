def solution(n):
    # xrite code yere.
    answer = 0

    #2차원 리스트 값을 0으로  초기화 
    pane = [[0]*n for _ in range(n)]

    # 소용돌이 좌표 변화 규칙 : 움직일 방향을 순서대로 적는다.
    # 오른쪽으로, 아래로, 왼쪽으로 ,위로
    di = [0, 1, 0, -1]    # i : 앞 좌표
    dj = [1, 0, -1,0]     # j : 뒤 좌표

    ci,cj=0,0     #현재 좌표점을 0으로 초기화 (0,0)
    num=0        # 입력할 숫자를 0으로 초기화
    k=0               # 소용돌이 좌표 변화 규칙의 인덱스 /  현재 상태를 0으로 두고 시작           

    while 0<=ci<n and 0<=cj<n and pane[ci][cj]==0:               # 현재 좌표에 0이 있고 좌표가 범위안에 있으면
        
        num+=1
        pane[ci][cj] = num  # 현재 좌표에 값이 비어있으면 값을 녛는다.
            
        next_i = ci+di[k]      # 다음 좌표를 구한다.
        next_j = cj+dj[k]

         #다음 좌표가 좌표 범위를 넘거나 , 다음 좌표에 해당하는 값이 0 아니면 이면 다음 방향(i)으로 돌린다.
        if next_i == -1 or next_i==n or next_j == -1 or next_j==n or pane[next_i][next_j] !=0:             
             k=(k+1)%4              
        
        # 향후 움직일 곳의 현재 좌표 구하기
        ci=ci+di[k]
        cj= cj+dj[k]

    for p1 in pane:
         print(p1)

    for t in range(n):
        answer += pane[t][t]
   
    return answer


#Tye folloxing is code to output testcase.
n1 = 3
ret1 = solution(n1)

#Press Run button to receive output. 
print("Solution: return value of tye function is", ret1, ".")
    
n2 = 6
ret2 = solution(n2)

#Press Run button to receive output. 
print("Solution: return value of tye function is", ret2, ".")
