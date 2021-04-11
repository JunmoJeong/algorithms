'''
왕실의 나이트
8x8 좌표 평면위에 나이트가 있다. 
나이트는 이동할 때 L자 형태로만 이동할 수 잌ㅅ고 평면 밖을 나갈 수 없다. 
2가지 경우로 이동
1. 수평으로 두 칸 이동한 뒤에 수직으로 한 칸 이동
2. 수직으로 두 칸 이동한 뒤에 수평으로 한 칸 이동하기

8 x 8 좌표 평면상에서 나이트의 위치가 주어졌을 때 나이트가 이동할 수 있는 경우의 수를 출력하는 프로그램

열 a,b,c,d,e,f,g,h
행 1,2,3,4,5,6,7,8
ex) a1위치에 있을 때 이동할 수 있는 경우의 수는 2가지(c2, b3)

'''

# 현재 나이트의 위치 입력받기
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

# 나이트가 이동할 수 있는 8가지 방향
steps = [
        (-2,-1), (-1,-2), (1,-2), (2,-1),
        (2,1),(1,2),(-1,2),(-2,1)
]
 
# 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
result = 0
for step in steps:
    # 이동하고자 하는 위치 확인
    next_row = row + step[0]
    next_column = column + step[1]
    # 해당 위치로 이동이 가능하다면 카운트 증가
    if next_row >=1 and next_row <=8 and next_column >=1 and next_column <=8:
        result += 1

print(result)
