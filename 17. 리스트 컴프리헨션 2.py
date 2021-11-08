a=[i for i in range(10) if i%3==0]
print(a)





#=============


a=['즐거운','행복한']
b=['파이썬','나']

c=[]

for i in a:
    for j in b:
        c.append(i+j)

print(c)

d=[]
d=[i+j for i in a for j in b]

print(d)
