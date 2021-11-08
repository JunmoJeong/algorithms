# immutable

a=10
b=a
print(id(a),a,b)
print(id(b),a,b)
a=20
print(id(a),a,b)
print(id(b),a,b)


# mutable

c=[1,2,3]
d=c
print(id(c),id(d),c,d)
c[2]=5
print(id(c),id(d),c,d)
