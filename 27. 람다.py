#람다 함수식
def func(a,b):
    return a+b
s=func(10,20)
print(s)

s1=lambda a,b:a+b
print(s1(10,20))


#객체에 람다를 이용해 메소드 추가
class Test:
    pass

t=Test()
t.add_method = lambda : print("메소드 추가")
t.add_method()


