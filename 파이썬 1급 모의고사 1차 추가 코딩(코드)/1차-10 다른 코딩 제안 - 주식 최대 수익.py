def solution(prices):
    answer = -1000000001   #answer 최대 수익
  
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            tmp_profit = prices[j]-prices[i]
            answer=max(answer,tmp_profit)

    return answer

#The following is code to output testcase. The code below is correct and you shall correct solution function.
prices1 = [1, 2, 3];
ret1 = solution(prices1);

#Press Run button to receive output.
print("Solution: return value of the function is", ret1, ".")
    
prices2 = [3, 1];
ret2 = solution(prices2);

#Press Run button to receive output.
print("Solution: return value of the function is", ret2, ".")
