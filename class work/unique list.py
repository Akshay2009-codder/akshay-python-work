list = [1,2,4,2,3,4,6,7,8,9,0,9,8,7,7,6]
result = []

for i in list:
    if i not in result:
        result.append(i)

print ("Unique list: " ,result)