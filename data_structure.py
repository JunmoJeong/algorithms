import queue

data_queue = queue.Queue()
data_queue.put(1)
data_queue.put("funcoding")
print(data_queue.qsize())
