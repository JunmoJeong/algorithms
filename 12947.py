'''
문제 : 양의 정수 x가 하샤드 수이면 x의 자릿수의 합으로 x가 나누어져야 한다. 
예를 들어 18의 자릿수 합은 1+8=9, 18은 9로 나누어 떨어지므로 18은 하샤드 수이다. 
자연수 n을 입력받아 n이 하샤드 수인지 아닌지 검사하는 함수 solution 
'''

# solution : 입력값을 정수형으로 받기 때문에 반복문을 사용하기 위해서 반복가능한 객체(iterable)
# 문자열로 바꿔서 반복문을 사용해야 한다. 이후 다시 정수형으로 바꿔서 각 자릿수의 합을 구했으며
# 나머지 연산자(%)을 사용해서 하샤드 수인지 검사한다. 

def solution(x):
    add=0
    for i in str(x):
        add += int(i)
    if x%add == 0:
        answer = True
    else:
        answer = True
    return answer

print(solution(18))
        