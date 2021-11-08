def solution(arrA, arrB):

    answer=sorted(arrA+arrB)

    return answer    

arrA = [-2, 3, 5, 9]
arrB = [0, 1, 5]
ret = solution(arrA, arrB);

#Press Run button to receive output.
print("Solution: return value of the function is ", ret, " .")
