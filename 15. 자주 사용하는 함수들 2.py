x=['a','b','c']

e1=enumerate(x)
print(e1,type(e1))
e=list(enumerate(x))
print(e)

for i,v in enumerate(x):
    print(i,v)


for a,b in zip(x1,x2):
    print(a,b)

    
