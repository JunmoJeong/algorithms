'''
x="10010"
y="110"

cnt=0

max_length=max(len(x), len(y))

x='0'*(max_length-len(x))+x
y='0'*(max_length-len(y))+y

for a,b in zip(x,y):
    if a!=b:
        cnt+=1

print(cnt)
'''





'''



s1=18; s2=6

print(bin(s1))
print(bin(s2))
print(bin(s1^s2))
print(bin(s1^s2).count('1'))














'''


x="10010"
y="00110"

x=int(x,2)
y=int(y,2)
print(format(x,'b'))
print(format(y,'b'))

print(bin(x&y),bin(x|y))
print(bin(x^y).count('1'))


























