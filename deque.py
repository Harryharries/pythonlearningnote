from collections import deque 

queue = deque()

queue.append(4)
queue.append(5)
queue.append(6)

print(queue)

queue.insert(2,9)
queue.popleft()
for i in queue:
    print(i)