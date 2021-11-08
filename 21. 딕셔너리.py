m={"1반":27,"2반":28,"3반":27}
print(m["2반"])

for i in m:
    print(i , " : ", m[i])

m["3반"]=40

print(m)

m2={"A":27,"B":28,"C":27}
print(m2)

m3= dict(A=2,B=28,C=27)
print(m3)

m4= dict(A반=2,B반=28,C반=27)
print(m4)

#-----------------------------

print(m.keys())

print(m.values())

print(m.items())



chg_list1=list(m.values())
print(chg_list1)

chg_list2=list(m.keys())
print(chg_list2)

chg_list3=list(m.items())
print(chg_list3)

