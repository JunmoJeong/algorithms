#iterable 객체
for i in range(3):
    print(i, end=' ')

for i in ['토요일','일요일']:
    print(i, end=' ')

print()

#iterator 객체
x=['토요일','일요일']
print(type(x))

x=iter(x)
print(type(x))

y=next(x)
print(y)

y=next(x)
print(y)

y=next(x)
print(y)
