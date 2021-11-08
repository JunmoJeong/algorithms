import math
import time

def solution(a, b):
    answer = 0
    # n을 제곱(세제곱)한 경우까지만 필요 int(math.sqrt(b))
    end = int(math.sqrt(b))
    arr = [True] * (end + 1)
    for n in range(2, end+1):
          if arr[n] == True:  # n이 소수인 경우
            for j in range(n + n, end + 1, n):  # n이후 n의 배수들을 False 판정
                arr[j] = False

    # print(arr)
    for i in range(2, len(arr)):
        if arr[i] == True:
            if a <= i ** 2 <= b:
                answer += 1
            #  print(i,i**2)
            if a <= i ** 3 <= b:
                answer += 1
            #   print(i,i**3)

    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
start=time.time()
a =  6
b =  1000000000
ret = solution(a, b)
end=time.time()
print(end-start)
#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")
