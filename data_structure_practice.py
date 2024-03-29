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


# 중간 삽입
node3 = Node(1.5)
node = head
search = True
while search:
    if node.data == 1:
        search = False
    else:
        node = node.next

node_next = node.next
node.next = node3
node3.next = node_next


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class NodeMgmt:
    def __init__(self, data):
        # 맨 앞의 node 주소는 알고 있어야 한다. head
        self.head = Node(data)

    def add(self, data):
        if self.head == '':
            self.head = Node(data)
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(data)

    def desc(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next


linkedlist1 = NodeMgmt(0)
linkedlist.desc()

for data in range(1, 10):
    linkedlist1.add(data)
linkedlist1.desc()


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class NodeMgmt:
    def __self__(self, data):
        self.head = Node(data)

    def add(self, data):
        if self.head == "":
            self.head = Node(data)
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(data)

    def desc(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next

    def delete(self, data):
        if self.head == "":
            print("해당 값을 가진 노드가 없습니다.")
            return

        if self.head.data == data:
            temp = self.head
            self.head = self.head.next
            del temp
        else:
            node = self.head
            while node.next:
                if node.next.data == data:
                    temp = node.next
                    node.next = node.next.next
                    del temp
                else:
                    node = node.next


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class NodeMgmt:
    def __init__(self, data):
        if self.head == "":
            self.head = Node(data)

    def add(self, data):
        if self.head == '':
            self.head = Node(data)
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(data)

    def desc(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next


def delete(self, data):
    if self.head = '':
        print("no node")
        return
    if self.head.data == data:
        temp = self.head
        self.head = self.head.next
        del temp
    else:
        node = self.head
        while node.next:
            if node.next.data == data:
                temp = node.next
                node.next = node.next.next
                del temp
                return
            else:
                node = node.next


# check
print(linkedlist1.head)
linkedlist1.delete(0)
linkedlist1.head
# 새로운 노드
linkedlist1 = NodeMgmt(0)
linkedlist1.desc()

# 여러 노드 출력
for data in range(1, 10):
    linkedlist1.add(data)
linkedlist1.desc()
linkedlist1.delete(4)
linkedlist1.desc()


class Node:
    def __init__(self, data, prev=None, next=None):
        self.prev = prev
        self.data = data
        self.next = next


class NodeMgmt:
    def __init__(self, data):
        self.head = Node(data)
        self.tail = self.head

    def insert(self, data):


class Node:
    def __init__(self, data, prev=None, next=None):
        self.prev = prev
        self.data = data
        self.next = next


class NodeMgmt:
    def __init__(self, data):
        self.head = Node(data)
        self.tail = self.head

    def insert(self, data):
        if self.head = None:
            self.head = Node(data)
            self.tail = self.head
        else:
            node = self.head
            while node.next:
                node = node.next
            new = Node(data)
            node.next = new
            new.prev = node
            self.tail = new

        def desc(self):
            node = self.head
            while node:
                print(node.data)
                node = node.next


double_linked_list = NodeMgmt(0)
for data in range(1, 10):
    double_linked_list.insert(data)

double_linked_list.desc()


def search_from_head(self, data):
    if self.head == None:
        return False
    node = self.head
    while node:
        if node.data == data:
            return node
        else:
            node = node.next
    return False


def insert_before(self, data, before_data):
    if self.head == None:
        self.head = Node(data)
        return True
    else:
        node = self.tail
        while node.data != before_data:
            node = node.prev
            if node == None:
                return False

        new = Node(data)
        before_new = node.prev
        before_new.next = new
        new.prev = before_new
        new.next = node
        node.prev = new

        return True


# retrun True
hash_table = list([0 for in range(8)])


def get_key(data):
    return h == ash(data)


def hash_function(key):
    return key % 8


def save_data(data, value):
    hash_address = hash_function(get_key(data))


hash_table = list([0 for i in range(8)])


def get_key(data):
    return hash(data)
def hash_function(key)
return key % 8


def save_data(data, value):
    index_key = get_key(data)
    hash_address = hash_function(index_key)
    if hash_table[hash_address] != 0:
        for index in range(len(hash_table[hash_address])):
            if hash_table[hash_address][index][0] == index_key
            hash_table[hash_address][index][1] = value
            return
        hash_table[hash_address].append([index_key, value])
    hash_table[hash_address] = Value


def read_data(data):
    hash_address = hash_function(get_key(data))
    return hash_table[hash_address]

#-*- coding: utf-8 -*-
import boto3
from PIL import Image
import numpy as np
import io
import os
import json

from tensorflow.python.keras.metrics import top_k_categorical_accuracy
from tensorflow.python.keras.models import load_model

from gevent.pywsgi import WSGIServer

def read_json(path):
    with open(path) as file:

def prepare_image(img):
    
