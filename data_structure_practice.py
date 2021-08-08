# 리스트 변수로 큐를 다루는 enqueue, dequeue 기능 구현

queue_list = list()


def enqueue(data):
    queue_list.append(data)


def dequeue():
    data = queue_list[0]
    del queue_list[0]
    return data


for index in range(10):
    enqueue(index)

print(len(queue_list))


def recursive(data):
    if data < 0:
        print("ended")
    else:
        print(data)
        recursive(data-1)
        print("returned", data)


data_stack = list()

data_stack.append(1)
data_stack.append(2)

data_stack.pop()

stack_list = list()


def push(data):
    stack_list.append(data):


def pop():
    data = stack_list[-1]
    del stack_list[-1]
    return data


for index in range(10):
    push(index)

pop()  # 맨 마지막 데이터가 출력


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


node1 = Node(1)
node2 = Node(2)
node1.next = node2
head = node1

# data 추가


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def add(data):
    node = head
    while node.next:  # next가 있다면
        node = node.next

    node.next = Node(data)


node1 = Node(1)
head = node1
for index in range(2, 10):
    add(index)

for i in range(2, 10):
    print(i)

node = head
while node.next:
    print(node.data)
    node = node.next

print(node.data)
