#다음과 같이 import를 사용할 수 있습니다.
import math
import time

def solution(a, b):
    answer = 0
    # n을 제곱(세제곱)한 경우까지만 필요 math.ceil(math.sqrt(b))
    for n in range(2,int(math.sqrt(b))+1):
        prime=True
        for i in range(2,n):      
            if n%i == 0:           # 자기 자신 이외의 약수가 존재하면
                prime=False        # 소수가 아님
                break
        else:
           # 소수의 제곱 수가 범위 안에 들어가면 갯수 증가
            if a<=n**2 <= b and prime==True:
                answer+=1
                print(n,"^2", n ** 2)
            # 소수의 세제곱 수가 범위 안에 들어가면 갯수 증가
            if a<=n**3 <= b and prime==True:
                answer+=1
                print(n,"^3", n ** 3)
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
start=time.time()
a =  6
b =  30
ret = solution(a, b)
end=time.time()
print(end-start)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")
