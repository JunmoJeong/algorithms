#피보나치 수열- 재귀함수 recursion

def fibo_r(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibo_r(n - 1) + fibo_r(n - 2)

import time
start=time.time()
print(fibo_r(40))
end=time.time()
print(end-start)