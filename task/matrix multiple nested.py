a = [[1,4],[3,8]]
b = [[8,78],[89,98]]
c = [[0,0],[0,0]]

for i in range(len(a)):
    for j in range(len(b[0])):
        for k in range(len(b)):
            c[i][j] += a[i][k]*b[k][j]

print(c)