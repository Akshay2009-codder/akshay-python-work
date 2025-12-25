# impliment stack

stack = []

# push in stack

stack.append(1)
stack.append(2)
stack.append(3)

print("Stack after push : ",stack)
print("top elment of stack : ",stack[-1])

# pop in stack

stack.pop()

print("Stack after pop : ",stack)


# is empty

if len(stack) == 0:
    print("Stack is empty")
else:
    print("Stack is not empty")