
def solution(num):
    next_num =num


    while True:
        next_num+=1
        length= len(str(next_num))
        if length%2 == 1:
            continue

       sep = int(length/2)
       cnt=1
       for s in str(next_num):
           
           front_sum+= int(s)
           
                 
        front_sum = func_c(front)
        back_sum = func_c(back)

        if front_sum == back_sum:
            break
    return next_num - num

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
num1 = 1
ret1 = solution(num1)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

num2 = 235386
ret2 = solution(num2)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")
