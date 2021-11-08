# 다음과 같이 import를 사용할 수 있습니다.
# import math

def step(n):
    step1=1
    step2=2
    step3=4
    new_step=0

    if n==3:
        return step3
    elif n>=4:
        for i in range(4,n+1):
            new_step=step1+step2+step3
            step1=step2
            step2=step3
            step3=new_step
        return new_step


#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
ret=step(6)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")
