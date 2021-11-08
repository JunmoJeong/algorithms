#immutable
a=10
b=a
print(id(a),a)
print(id(b),b)

a=20
print(id(a),a)
print(id(b),b)

#mutable
c=[1,2,3]
d=c
print(id(c),c)
print(id(d),d)

c[2]=4
print(id(c),c)
print(id(d),d)
