# 다음과 같이 import를 사용할 수 있습니다.
# import math

def step(n):
    if n==1:
        return 1
    elif n==2:
        return 2
    elif n==3:
        return 4
    elif n>=4:
        return step(n-1)+step(n-2)+step(n-3)


#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
ret=step(6)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")
