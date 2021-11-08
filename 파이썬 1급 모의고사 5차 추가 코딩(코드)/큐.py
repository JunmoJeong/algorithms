#리스트를 이용한 큐 구현
queue=[]

queue.append(1)
queue.append(2)
queue.append(3)
print(queue)

queue.pop(0)
print(queue)
queue.pop(0)
print(queue)

#데크를 이용한 큐 구현
from collections import deque

queue2=deque()
queue2.append(1)
queue2.append(2)
queue2.append(3)
print(queue2)

queue2.popleft()
print(queue2)
queue2.popleft()
print(queue2)


#큐를 이용한 큐 구현
from queue import Queue

queue3=Queue(maxsize=3)
queue3.put(1)
queue3.put(2)
queue3.put(3)
print("큐 Size:", queue3.qsize())

print(queue3.get())
print(queue3.get())
print("큐 Size:", queue3.qsize())

