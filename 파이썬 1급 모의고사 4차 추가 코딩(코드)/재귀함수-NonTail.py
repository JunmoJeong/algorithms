# non tail recursive function
def f(n):
    if n<=1:
        return 1
    print(n, "! 을 구합니다")
    return n*f(n-1)


print(f(4))

