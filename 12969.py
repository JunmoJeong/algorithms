'''
입력으로 두 개의 정수 n과 m이 주어진다. 
* 문자를 이용해 가로 길이 n, 세로 길이가 m인 직사각형 형태를 출력
'''

# 풀이 : 반복문을 돌리기 위해 n,m을 int형으로 바꾼다. 우선 두 개의 입력이 공백을 사이에 두고 받으므로
# split을 이용해 분리하여 받는다. 

# input으로 받는 값들은 string 자료형을 가지고 있으므로 int형으로 바꿔야 한다. 

a, b = map(int, input().split(' '))
answer =''
for i in range(b):
    for j in range(a):
        answer +="*"
    answer += '\n'
print(answer)
