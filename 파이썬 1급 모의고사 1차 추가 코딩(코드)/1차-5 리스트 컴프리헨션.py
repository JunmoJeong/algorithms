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
