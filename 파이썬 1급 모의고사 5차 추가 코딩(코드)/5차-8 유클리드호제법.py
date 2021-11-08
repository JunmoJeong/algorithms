#최대공약수 구하기-유클리드 호제법
def gcd(a,b):
    r=a%b
    print(a, b, r)
    while r>0:
        a=b
        b=r
        r=a%b
        print(a, b, r)

    return b

print(gcd(72,27))

#최대공약수 구하기-유클리드 호제법 재귀호출
def gcd2(a,b):
    if b==0:
        return a
    else:
        print(a,b,a%b)
        return gcd2(b,a%b)
    return b

print(gcd2(72,27))
