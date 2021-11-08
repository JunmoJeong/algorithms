#최대공약수 구하기
def gcd(a,b,c):
    answer=0
    i=1
    while i<=a and i<=b and i<=c:
        if a%i==0 and b%i==0 and c%i ==0:
            answer =i
        i+=1
    return answer

print(gcd(24,9,15))

#공약수의 개수 구하기
def cm_cnt(a,b,c):
    answer=0
    i=1
    while i<=a and i<=b and i<=c:
        if a%i==0 and b%i==0 and c%i ==0:
            answer +=1
        i+=1
    return answer

print(cm_cnt(24,9,15))

