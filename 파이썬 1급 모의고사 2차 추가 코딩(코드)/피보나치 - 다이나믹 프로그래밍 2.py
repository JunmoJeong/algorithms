import time
dp=[1,1]

def fibo_dp(n):
    for i in range(2,n):
        dp.append(dp[i-1] + dp[i-2])
    return dp[n-1]


start=time.time()
print(fibo_dp(100))
end=time.time()
print(end-start)
