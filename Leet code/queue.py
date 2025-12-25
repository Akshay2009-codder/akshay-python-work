# impliment queue

queue = []

# enque

queue.append(1)
queue.append(2)
queue.append(3)

print ("Queue : ", queue)


# dequeue

pop = queue.pop(0)
print ("Popped element : ", pop)
print ("Queue after pop : ", queue)
print ("Top element : ", queue[0])

# is empty

if len(queue) == 0:
    print("Queue is empty")
else:
    print("Queue is not empty")