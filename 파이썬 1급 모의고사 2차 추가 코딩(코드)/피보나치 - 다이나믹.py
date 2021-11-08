dp = [0 for _ in range(500)]

def fibo_r(n):
    if n == 1 or n == 2:
        return 1
    if dp[n] !=0:
        return dp[n]
    else:
        dp[n]=fibo_r(n - 1) + fibo_r(n - 2)
        return dp[n]

import time
start=time.time()
print(fibo_r(40))
end=time.time()
print(end-start)