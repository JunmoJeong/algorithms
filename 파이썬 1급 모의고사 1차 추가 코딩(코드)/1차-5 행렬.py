a=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]


for i in range(4):
    for j in range(4):
        a[i][j]= '(' + str(i) + ',' + str(j)+ ')'
    print(a[i], end="\n")





a=[[0]*4 for _ in range(4)]
