def solution(commands):
    answer = [0, 0]
    rule = {'L': (-1, 0), 'R': (1, 0), 'U': (0, 1), 'D': (0, -1)}

    print( rule["L"],rule["L"][0],rule["L"][1] )

    for c in commands:
        answer[0] += rule[c][0]
        answer[1] += rule[c][1]
    return answer


commands = "URDDL"
ret = solution(commands)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은 ", ret, " 입니다.")