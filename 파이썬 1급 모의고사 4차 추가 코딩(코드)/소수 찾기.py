k=1000
arr=[]
for n in range(2,k+1):
    for i in range(2,n):
        if n%i ==0:
            break
    else:
      arr.append(n)

print(arr)