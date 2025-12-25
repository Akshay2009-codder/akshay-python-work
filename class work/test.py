def infixToPostfix(infix):
    stack = []
    output = ""
    pre =  {"+":1,"-":1,"*":2,"/":2}

    for char in infix:
        if char.isalnum():
            output += char
        elif char in pre:
            while stack and pre.get(stack[-1],0) >= pre[char]:
                output += stack.pop()
            stack.append(char)
    return output
