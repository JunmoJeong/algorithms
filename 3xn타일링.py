def solution(n):
    arr = [0]*(n+1)
    arr[2] = 3
    sum_value = 0
    for i in range(4, (n+1), 2):
        sum_value += arr[i-4]
        arr[i] = (arr[i-2]*3+sum_value*2+2) % 100000007
    return arr[n]
