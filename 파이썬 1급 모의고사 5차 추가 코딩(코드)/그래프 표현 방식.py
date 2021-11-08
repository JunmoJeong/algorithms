
# E ={(0,1),(0,2),(1,2),(2,2)}

# 인접 리스트 방식
gl=[[] for _ in range(3)]

gl[0].append(1)
gl[0].append(2)

gl[1].append(2)

gl[2].append(2)

print(gl)

#인접 행렬 방식
gm = [
    [0,1,1],
    [0,0,1],
    [0,0,1]
]

print(gm)