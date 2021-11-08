def recursive(i):
  if i==3:
    return
  
  print(i,"번째 재귀함수 실행", i+1,'번째 재귀함수 호출')
  recursive(i+1)
  print(i,'번째 재귀함수 종료')

recursive(1)





