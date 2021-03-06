'''
시각
정수 N이 입력되면 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서
3이 하나라도 포함되는 몯ㄴ 경우의 수를 구하는 프로그램을 작성하시오.

ex) 입력 1일 때 3이 포함되는 경우는
00시 00분 03초, 00시 13분 30초 등등

하루는 86400초이기 때문에 모든 경우의 수 86400가지밖에 존재하지 않음.
단순히 시각을 1씩 증가시키면서 3이 하나라도 포함되어 있는지 확인하면 된다.
전체 시, 분, 초에 대한 경우의 수는 24 * 60 * 60이고 3중 반복문을 이용해 계산할 수 있다.

매 시각을 문자열로 바꾼 다음 문자열에 '3'이 포함됐는지 검사
ex) 03시 20분 35초일 때 이를 032035로 만들어서 체크

'''
# 시간 입력받기
h = int(input())

count = 0
for i in range(h+1):
    for j in range(60):
        for k in range(60):
            # 매 시간 안에 '3'이 포함되어 있다면 카운트 증가
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)


