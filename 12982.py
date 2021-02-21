'''
https://programmers.co.kr/learn/courses/30/lessons/12982

문제 : 부서별로 신청한 금액이 들어있는 배열 d와 예산 budget이 매개변수로 주어질 때,
최대 몇 개의 부서에 물품을 지원해 줄 수 있는지 return 하도록 solution 함수를 완성해보기
'''

# 풀이 : 최대한 많은 부서에게 예산을 분배하는 것이 목적이기 때문에, 
# 큰 금액을 신청한 부서에게는 지원하지 않을 때 더 많은 부서에게 예산을 분배를 할 수 있다. 
d = [100,200,300,500]
budget = 2000
def solution( d, budget):
    while len(d) > 0:
        if sum(d) <= budget:
            return len(d)
        else:
            d.remove(max(d))
    return 0
print(solution(d,budget))