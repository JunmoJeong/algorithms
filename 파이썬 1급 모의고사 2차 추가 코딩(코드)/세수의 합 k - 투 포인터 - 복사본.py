#세 개의 수의 합이 K 인 것 - n의 2제곱 시간

def solution(arr, K):
    answer = 0;     total=0
    arr.sort()

    for p in range(len(arr)-2):
        left, right = p + 1, len(arr) - 1

        while left<right:
            total = arr[p] + arr[left] + arr[right]
            if total < K:
                left+=1
            elif total >K:
                right-=1
            else:
                answer += 1
                print(arr[p], arr[left], arr[right])
                left+=1
                right-=1
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
arr = [1, 5, 3, 8, 2, 4]
K = 9
ret = solution(arr, K)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은 ", ret, " 입니다.")
