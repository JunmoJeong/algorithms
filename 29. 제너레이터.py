
#제너레이터 함수
def gen():
    print("첫 번째 ")
    yield 
    print("두 번째 ")
    yield 2

g=gen()
y1=next(g)
print(y1)

y2=next(g)
print(y2)

#제너레이터 표현식
def gen2():
    d=[10,20,30]
    yield from d

g2=gen2()
print(next(g2))
print(next(g2))
