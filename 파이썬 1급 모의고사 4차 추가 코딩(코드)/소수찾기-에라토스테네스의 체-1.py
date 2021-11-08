#소수 찾기-에라토스테네스의 체-1.py
import time
import math

def prime_list(n):
    # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
    arr = [True] * (n+1)

    # n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
    end=int(math.sqrt(n))

    for i in range(2, end + 1):
        if arr[i] == True:           # i가 소수인 경우
            for j in range(i+i, n+1, i): # i이후 i의 배수들을 False 판정
                arr[j] = False

    # 소수 목록 산출
    return [i for i in range(2,n+1) if arr[i]==True ]


start=time.time()
prime=prime_list(1000000000)
end=time.time()
print(end-start)

print(prime)
print("\n\n", len(prime), "개의 소수가 있습니다.")