
def func_step(steps,n):
    if steps[n]>0:
        return steps[n]

    if n==1:
       steps[n]=1
    elif n==2:
        steps[n]=2
    elif n==3:
        steps[n]=4
    else:
        steps[n]=func_step(steps,n-1)+func_step(steps,n-2)+func_step(steps,n-3)

    return steps[n]

step=6
ret=func_step([0]*(step+1),step)

print("solution 함수의 반환 값은", ret, "입니다.")
