'''
문제 : x만큼 간격이 있는 n개의 숫자

'''

# solution : 정수 x와 자연수 n을 입력 받아, x부터 시작해 x씩 증가하는 숫자를 n개 지니는 리스트를 리턴
# x부터 시작해 n번 반복하는 작업이므로 반복문을 사용하여 answer 리스트에 추가하면 된다. 

def solution(x, n):
    answer = []
    for i in range(n):
        answer.append(x*(i+1))
    return answer

print(solution(3,6))