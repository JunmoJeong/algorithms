#리스트를 이용한 스택 구현
stack=[]

stack.append(1)
stack.append(2)
stack.append(3)
print(stack)

stack.pop()
print(stack)
stack.pop()
print(stack)

#데크를 이용한 스택 구현
from collections import deque

stack2=deque()
stack2.append(1)
stack2.append(2)
stack2.append(3)
print(stack2)

stack2.pop()
print(stack2)
stack2.pop()
print(stack2)

#LIFO큐를 이용한 스택 구현
from queue import LifoQueue

stack3=LifoQueue(maxsize=3)
stack3.put(1)
stack3.put(2)
stack3.put(3)
print("스택 Size:", stack3.qsize())

print(stack3.get())
print(stack3.get())
print("스택 Size:", stack3.qsize())
