def infixToPostfix(expression):

  precedence = {'+':1,'-':1,'*':2,'/':2}
  stack = []
  output = ''

  for char in expression:
      if char.isalnum():
          output += char
      elif char in precedence:
          while stack and precedence.get(stack[-1],0) >= precedence[char]:
              output += stack.pop()
          stack.append(char)
  while stack:
      output += stack.pop()
  return output

print(infixToPostfix("A+B*C-D/E+F*G"))
