 '''
숫자 카드 게임
여러 개의 숫자 카드 중에서 가장 높은 숫자가 쓰인 카드 한 장을 뽑는 게임
N x M 형태로 카드를 놓고 뽑고자 하는 카드가 포함되어 있는 행을 선택
그 다음 선택된 행에 포함된 카드들 중 가장 숫자가 낮은 카드를 뽑는다. 

처음에 카드를 골라낼 행을 선택할 때 이후에 해당 행에서 가장 숫자가 낮은 카드를 뽑을 것을 고려하여 최종적으로 가장 높은 숫자의 카드를 
뽑을 수 있는 전략을 세워야 한다. 

Sol) 각 행마다 가장 작은 수를 찾은 뒤에 그 수 중에서 가장 큰 수를 찾는 것.

입력 
3 3 
3 1 2
4 1 4
2 2 2

출력 2


 '''

# min() 함수를 이용
n , m = map(int, input().split())

result = 0

# 한 줄씩 입력받아 확인
for i in range(n):
    data = list(map(int, input().split()))
    # 현재 줄에서 가장 작은 수 찾기
    min_value = min(data)
    # 가장 작은 수들 중에서 가장 큰 수 찾기
    result = max(result, min_value)

print(reuslt)


# 2중 반복분 
n, m = map(int, input().split())

result = 0

for i in range(n):
    data = list(map(int, input().split()))
    # 현재 줄에서 가장 작은 수 찾기
    min_value = 10001
    for a in data:
        min_value = min(min_value, a)
     
    # 가장 작은 수들 중에서 가장 큰 수 찾기
    result = max(result, min_value)

print(result)


