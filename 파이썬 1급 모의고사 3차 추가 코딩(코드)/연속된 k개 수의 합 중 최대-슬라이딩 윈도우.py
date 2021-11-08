def solution(arr, k) :
    answer = 0
    rsum = sum(arr[0:k])
    answer = rsum
    for i in range(k,len(arr)) :
        rsum = rsum - arr[i - k] + arr[i]
        answer=max(answer,rsum)
    return answer

arr1 = [1, 1, 9, 3, 7, 6, 5, 10]
k1 = 4
ret1 = solution(arr1, k1)


print("solution 함수의 반환 값은 ", ret1, " 입니다.")

