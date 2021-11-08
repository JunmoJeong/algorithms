#packing
p=(10,20)
print(p)

p2= 30,40
print(p2)

 
#unpacking
p3=(10,20)
u1,u2=p3
print(u1,u2)

#unpacking  ,  packing: *
p4=(10,20,30,40,50)
u1,u2,*u3=p4
print("u1:" , u1, "u2:" , u2, "u3:" , u3 )

print( type(u1), type(u3))


#함수에서의 packing
def func_pack():
    return 10,20

n1=func_pack()
print(n1)

#함수에서의 unpacking
def func_unpack(u1,u2,*u3):
    print("u1:" , u1, "u2:" , u2, "u3:" , u3 )
    print( type(u1), type(u3))

func_unpack(10,20,30,40,50)


# 딕셔너리
def func_unpack(u1,u2,*u3):
    print("u1:" , u1, "u2:" , u2, "u3:" , u3 )
    print( type(u1), type(u3))

d={"1반":27,"2반":28,"3반":27,"4반":30}
func_unpack(*(d.items()))

