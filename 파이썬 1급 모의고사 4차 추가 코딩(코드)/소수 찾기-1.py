#소수 찾기-1.py
import math
import time
def solution(k):
    arr=[]
    for n in range(2, k+1):
        prime=True
        for i in range(2, n):
            if n % i == 0:      # 자기자신 이외의 약수가 존재하면
                 prime=False
                 break
        if prime==True:
            arr.append(n)
    return arr



k =  100000
start=time.time()
ret = solution(k)
end=time.time()
print(end-start)

print(len(ret))
# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")
