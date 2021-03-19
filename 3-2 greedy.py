'''
"큰수의 법칙"
다양한 수로 이루어진 배열이 있을 때 주어진 수들을 M번 더하여 가장 큰 수를 만드는 법칙.
배열의 특정한 인덱스에 해당하는 수가 연속해서 K번을 초과하여 더해질 수 없는 것이 특징.

예)  2,4,5,4,6    M : 8, K : 3
6+6+6+5+6+6+6+5 = 46
서로 다른 인덱스에 해당하는 수가 같은 경우에도 서로 다른 것으로 간주
예 ) 3,4,3,4,3    M : 7, K : 2
4+4+4+4+4+4+4 = 28

'''

# 전형적인 그리디 알고리즘 문제
# 이 문제를 해결하려면 일단 입력값 중에서 가장 큰 수와 두 번째로 큰 수만 저장하면 된다.
'''
n, m, k = map(int, input().split())

data = list(map(int, input().split())
data.srot()
first = data[n-1] # 가장 큰 수
second = data[n-2] # 두 번째로 큰 수 

result = 0 

while True:
    for i in range(k): # 가장 큰 수 K번 더하기
        if m == 0
            break
        result += first
        m -= 1
    if m == 0: # m이 0이라면 반복문 탈출
        break
    result += second # 두 번째로 큰 수를 한 번 더하기
    m -= 1 # 더할 때마다 1씩 빼기

print(result)
'''

# 더 좋은 방법
# 반복되는 수열을 식으로 나타내본다.
# int(M / (K+1)) * K + M % (K + 1)

# N, M, K를 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())
# N개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

data.sort() # 입력받은 수 정렬
first = data[n-1]
second = data[n-2]

# 가장 큰 수가 더해지는 횟수 계산
count = int(m / (k+1)) * k
count += m% (k+1)

result = 0
result += (count) * first
result += (m-count) * second

print(result)
