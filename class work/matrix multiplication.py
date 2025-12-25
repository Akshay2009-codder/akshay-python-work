x = [[1,2],[3,4]]
y = [[5,6],[7,8]]

result = [[0,0],[0,0]]

for i in range (len(x)):
    for j in range (len(y[0])):
        for k in range (len(x)):
            result[i][j] += x[i][k] * y[k][j]

print (result)