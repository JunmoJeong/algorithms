#다음과 같이 import를 사용할 수 있습니다.
#import math

def solution(commands):
    answer=[0,0]
    rule=[(-1,0), (1,0),(0,1),(0,-1)]
    print(rule[0][0], rule[0])
    for c in commands:
        if c=="L":
            answer[0]+= rule[0][0]
            answer[1]+= rule[0][1]
        elif c=="R":
            answer[0]+= rule[1][0]
            answer[1]+= rule[1][1]
        elif c=="U":
            answer[0]+= rule[2][0]
            answer[1]+= rule[2][1]
        elif c=="D":
            answer[0]+= rule[3][0]
            answer[1]+= rule[3][1]
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
commands = "URDDL"
ret = solution(commands)
print("solution 함수의 반환 값은 ", ret, " 입니다.")

commands = "UR"
ret = solution(commands)
#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은 ", ret, " 입니다.")