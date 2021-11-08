def solution(pos):
    d = [(1,2),(1,-2),(-1,-2),(-1,2),(2,1),(2,-1),(-2,-1),(-2,1)]

    cx = ord(pos[0]) - ord("A")
    cy =int(pos[1])-1
    
    answer = 0
    
    for cd in d:
        nx = cx +cd[0]
        ny = cy + cd[1]
        if 0<=nx<8 and 0<=ny<8:
            answer += 1
    return answer


pos = "A7"
ret = solution(pos)

#Press Run button to receive output.
print("Solution: return value of the function is", ret, ".")


