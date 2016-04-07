from collections import deque

queue = deque(['1','2','3'])

queue.append("mike")
queue.append("ben")
queue.append("fucking pterodactyls")

print queue.popleft() # less expensive then a pop or list pop- doesn't require shifting by 1
print queue
