# 시작 : i인덱스 , 종료: i번 부터 4개
def solution(arr, k) :
    answer = 0

    for i in range(len(arr)-k+1) :
        rsum = 0
        for j in range(i,i+k):
            rsum+=arr[j]
        answer=max(answer,rsum)
    return answer

# 시작 : i인덱스 , 종료: i번 부터 갯수 4개를 세면서 합
def solution2(arr, k) :
    answer = 0
    for i in range(len(arr)-k+1) :
        rsum = 0
        for j in range(k):
            rsum+=arr[i+j]
        answer=max(answer,rsum)
    return answer

arr1 = [1, 1, 9, 3, 7, 6, 5, 10]
k1 = 4
ret1 = solution(arr1, k1)

print("solution 함수의 반환 값은 ", ret1, " 입니다.")

arr1 = [1, 1, 9, 3, 7, 6, 5, 10]
k1 = 4
ret1 = solution2(arr1, k1)

print("solution 함수의 반환 값은 ", ret1, " 입니다.")