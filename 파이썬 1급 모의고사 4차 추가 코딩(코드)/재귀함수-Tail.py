# tail recursive function
def f(n,a):
    if (n == 0):
        return a
    print(n,a," 실행")

    return f(n-1,n*a)

print(f(4,1))

