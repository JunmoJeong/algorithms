a=[0 for _ in range(5)]
print(a)

a=[0 for i in range(5)]
print(a)

a=[0]*5
print(a)

a=[i for i in range(5)]
print(a)

a=[str(i+10) for i in range(5)]
print(a)

a=list(i for i in range(3,10,2))
print(a)

a=[]
for i in range(5):
    a.append(i)
print(a)



n=3
m=4

a=[0]*2
print(a)
a= [i*2 for i in range(5)]
print(a)
a=[[0]*n for _ in range(m)]
print(a)
a= [[0 for _ in range(n)] for _ in range(m)]
a[1][2]=5
print(a)



a=[[0]*n]*m
a[1][2]=5
print(a)
