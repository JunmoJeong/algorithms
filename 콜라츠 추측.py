def solution(num):
    answer = 0

    while(answer < 500):
        if num == 1:
            break
        if num % 2 == 0:
            answer += 1
            num = num/2
        elif num % 2 == 1:
            answer += 1
            num = (num*3)+1

    if num != 1:
        answer = -1

    return answer
