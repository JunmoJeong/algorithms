import time

def solution1(arr, K):
    answer = 0
    n = len(arr)
    K=9

    for p in range(0, n-2):
        for q in range(p + 1, n-1):
            for r in range(q + 1, n):
                if (arr[p] + arr[q] + arr[r])  == K:
                    answer += 1
                    #print(arr[p], arr[q], arr[r])
    return answer

def solution2(arr, K):
    answer = 0;   sum=0
    arr.sort()

    for p in range(len(arr)-2):
        left, right = p + 1, len(arr) - 1

        while left<right:
            sum = arr[p] + arr[left] + arr[right]
            if sum < K:
                left+=1
            elif sum >K:
                right-=1
            else:
                answer += 1
                # print(arr[p], arr[left], arr[right])
                left+=1
                right-=1
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
arr = [1, 5, 3, 8, 2, 4]
K = 9

time_start=time.time()
for i in range(100000):
    ret = solution1(arr, K)
time_end=time.time()
print("브루트 포스:" , time_end-time_start)

time_start=time.time()
for i in range(100000):
    ret = solution2(arr, K)
time_end=time.time()
print("투 포인터:" , time_end-time_start)


#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은 ", ret, " 입니다.")
