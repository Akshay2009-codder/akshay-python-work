import numpy as np

matrix = np.random.randint(1, 12, size = (3,4))
print(matrix)

print("Transhport matrix :\n ", np.transpose(matrix))

flat = matrix.flatten()
print("Flatern : \n", flat)

reshaping = matrix.reshape(4,3)
print("reshaping : \n", reshaping)

