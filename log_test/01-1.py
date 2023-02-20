# 1~100 사이의 무작위값을 찾아 출력하는 코드
import random
findNumber = random.randrange(1,100)

for i in range(1,101):
    if i == findNumber:
        print(i)
        break
    