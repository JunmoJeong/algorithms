a=[9,3,1,15]
print("기본 a 데이터")
print(a,"\n")

# a.sort() : 오름차순. 리스트 순서 자체를 바꿈. 메소드
a.sort()                        
print("=== a.sort() 후 a ")
print(a,"\n")


a=[9,3,1,15]
# a.sort(reverse=True) : 내림차순. 리스트 순서 자체를 바꿈. 메소드
a.sort(reverse=True)                      
print("=== a.sort(reverse=True)  후 a ")
print(a,"\n")


# a.sort(key=str.lower) : 오름차순. 리스트 순서 자체를 바꿈. 메소드 .소문자로 변경해서 정렬 upper
a.sort(key=str.lower)
print("===== a.sort(key=str.lower) 후 a ")
print(a,"\n")


a=["apple","APPLE","key","KOREA"]
print("기본 a 데이터")
print(a)
print("기본 sorted: ", sorted(a))

a=[9,3,1,15]
# a.reverse() : 역순. 리스트 순서 자체를 바꿈. 메소드
a.reverse()    
print("=== a.reverse()  후 a ")
print(a,"\n")

                 
a=[9,3,1,15]
#  sorted(a)   :  오름차순. 리스트 자체의 순서를 바꾸지 않음, 함수 
print("=== sorted(a)")
print(sorted(a),"\n")        
print("=== sorted(a) 후 a " )
print(a,"\n")

a=[9,3,1,15]
#  sorted(a, reverse=True)   :  내림차순. 리스트 자체의 순서를 바꾸지 않음, 함수 
print(sorted(a, reverse=True),"\n")        
print("=== sorted(a) 후 a " )
print(a,"\n")

print("=== sorted(a,reverse=True) ")
a=[9,3,1,15]
b=[]
#  reversed(a)   :   역순.  리스트 자체의 순서를 바꾸지 않음, 함수 
print("=== reversed(a)")
print(reversed(a))
print(list(reversed(a)),"\n")
  
print("=== reversed(a) 후 a " )
print(a,"\n")

