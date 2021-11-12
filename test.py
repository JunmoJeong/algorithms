def solution(commands):
    current_position = [0, 0]
    for i in commands:
        if i == "L":
            current_position[0] += -1
        elif i == "R":
            current_position[1] += 1

    return current_position


commands = "URDDL"
ret = solution(commands)

print("solution 함수의 반환 값은 ", ret, "입니다")
