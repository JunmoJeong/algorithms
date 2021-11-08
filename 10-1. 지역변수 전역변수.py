x = 15
y=100

def varscope(): 
    global x 
    x = 20
    y = 30
    print("함수 안 x :", x)
    print("함수 안 y :", y)

varscope()
print("함수 밖-메인 x :", x)
print("함수 밖-메인 y :", y) 

