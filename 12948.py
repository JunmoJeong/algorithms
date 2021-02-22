'''
문제 : 모바일 개인정보 보호를 위해 전화번호 일부를 가려야 한다. 
전화번호가 문자열 phone_number로 주어졌을 때, 전화번호의 뒷 4자리를 제외한 나머지 숫자를
전부 *으로 가린 문자열을 리턴하는 함수, solution을 완성해라
'''

# solution : 무자열의 슬라이싱을 이용하는 문제.
# 뒷 4자리를 제외한 나머지를 가리는 것이기 때문에 뒤에서 부터 접근하는 슬라이싱을 알아야 한다. 
def solution(phone_number):
    answer = "*"*(len(phone_number)-4) + phone_number[-4:]
    return answer

print(solution("01093135413"))