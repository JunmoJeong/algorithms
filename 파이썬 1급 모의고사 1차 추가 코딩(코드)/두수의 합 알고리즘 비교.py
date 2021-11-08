a=[3,5,7,11,9]

#브루트 포스
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i]+a[j]==12:
            print(a[i], a[j])


#12에서 해당 값을 뺀 값이 들어있나 확인 12-3 =9, 9 가 있나 확인
        
for i,n in enumerate(a):
    if 12-n in a[i+1:]:
        print(n, 12-n)
