# <undefined>
# import <undefined>

def solution(num):
    answer = num+1
    digit = 1
    while answer // digit % 10 == 0:
         answer += digit
        digit *= 10
                
    return answer


num = 9949999;
ret = solution(num)

#Press Run button to receive output. 
print("Solution: return value of the function is", ret, ".")

