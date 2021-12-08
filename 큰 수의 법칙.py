'''n, m, k = map(int, input().split(' '))

data = list(map(int, input().split(' ')))

data.sort()
first = data[n-1]
second = data[n-2]

result = 0

while True:
    for i in range(k):
        if m == 0:
            break
        result += first
        m -= 1  # 더할 때마다 m에서 1씩 빼기
    if m == 0:
        break
    result += second
    m -= 1  # 더할 때마다 1씩 빼기
print(result)
'''
# N, M, K 를 공백으로 구분하여 입력받기
n, m, k = map(int, input().split(' '))

# N개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split(' ')))

data.sort()
first = data[n-1]  # 가장 큰 수
second = data[n-1]  # 두 번째로 큰 수

# 가장 큰 수가 더해지는 횟수 계산
count = int(m / (k+1)) * k + m % (k+1)

result = 0
result += (count) * first  # 가장 큰 수 더하기
result += (m-count) * second

print(result)
