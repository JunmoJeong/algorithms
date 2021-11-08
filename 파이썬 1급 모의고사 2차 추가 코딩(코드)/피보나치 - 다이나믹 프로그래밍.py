import time

dp=[0 for _ in range(500)]

def fibo_dp(n):

    if n<=2:
        return 1

    if dp[n]!=0:
        return dp[n]
    else:
        dp[n]=fibo_dp(n-1) + fibo_dp(n-2)
        return dp[n]

start=time.time()
print(fibo_dp(400))
end=time.time()
print(end-start)


'''
dp=[1,1]

def fibo_dp(n):
    a=1
    if n <= len(dp):
         return dp[n-1]
    else:
        temp=fibo_dp(n-1) + fibo_dp(n-2)
        print(temp)
        dp.append(temp)
        print(dp)
        return dp[n-1]



start=time.time()
print(fibo_dp(5))
end=time.time()
print(end-start)
'''
