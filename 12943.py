'''
문제 : 콜라츠 추측. 주어진 수가 1이 될떄까지 다음 작업을 반복하면 모든 수를 1로 만들수 있다. 
1. 입력된 수가 짝수라면 2로 나눈다. 
2. 입력된 수가 홀수라면 3을 곱하고 1을 더한다. 
2. 결과로 나온 수가 같은 작업을 1이 될때까지 반복한다. 

작업을 500번을 반복해도 1이 되지 않는다면 -1을 반환해라.
'''



# solution : 문제에 나와있는 대로만 하면 된다. 

def solution(num):
    answer = 0
    for i in range(500):
        if num == 1:
            return answer
        else:
            if num%2 == 0:
                num= num//2
                answer +=1
            else:
                num = num*3+1
                answer += 1
    return -1

