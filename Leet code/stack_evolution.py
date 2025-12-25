def evalute_stack(exp):
   stack = []
   for ch in exp:
       if ch.isdigit():
           stack.append(int(ch))
       else:
           b = stack.pop()
           a = stack.pop()

           if ch == "+":
               stack.append(a+b)
           elif ch == "-":
               stack.append(a-b)
           elif ch == "*":
               stack.append(a*b)
           elif ch == "/":
               stack.append(a/b)
   return stack.pop()


print(evalute_stack("53+82-*"))