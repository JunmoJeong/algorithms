#소수 찾기-2.py
import math
import time
def solution(k):
    arr=[]

    for n in range(2, k+1):
        for i in range(2, n):
            if n % i == 0:        # 자기 자신 이외의 약수가 존재하면
                 break
        else:                     # break문을 만나지 않고 정상종료 됐다면 소수
            arr.append(n)
    return arr


k =  100

start=time.time()
ret = solution(k)
end=time.time()
print(end-start)

print(len(ret))


# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")
