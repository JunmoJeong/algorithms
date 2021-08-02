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
