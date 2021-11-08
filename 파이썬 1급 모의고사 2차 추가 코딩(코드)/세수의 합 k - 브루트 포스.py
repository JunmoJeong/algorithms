#세 개의 수의 합이 K 인 것 - n의 3제곱 시간

def solution(arr, K):
    answer = 0
    n = len(arr)


    for p in range(0, n-2):
        for q in range(p + 1, n-1):
            for r in range(q + 1, n):
                if (arr[p] + arr[q] + arr[r])  == K:
                    answer += 1
                    print(arr[p], arr[q], arr[r])
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
arr = [1, 5, 3, 8, 2, 4]
K = 9
ret = solution(arr, K)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은 ", ret, " 입니다.")
