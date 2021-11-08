g=[[27,28,27,30],
      [30,29,27,29],
      [27,28,29,30]]

print("2학년 각 반의 인원수:", g[1])
print("2학년 3반 인원수:",g[1][2])

for i in range(3):
    for j in range(4):
        print(i+1,"학년",j+1,"반", g[i][j],"명")

for grade in g:
    print(grade)

for grade in g:
    for c in grade:
        print(c,end=' ')
    print()

for c1,c2,c3,c4 in g:
    print(c1,c2,c3,c4)

