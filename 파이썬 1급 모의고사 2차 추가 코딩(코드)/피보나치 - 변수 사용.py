
import time
def fibonacci(n):
    a = 1
    b = 1

    for i in range(2, n):
        a,b = b, a + b
        print(a,b)
    return b

start=time.time()
print(fibonacci(8))
end=time.time()
print(end-start)

