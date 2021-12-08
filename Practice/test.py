from queue import Queue 

q = Queue(maxsize = 5)

q.put(111)

print(q.get())