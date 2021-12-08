n, m, k = map(int, input().split(' '))

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
