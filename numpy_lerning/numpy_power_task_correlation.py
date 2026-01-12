import numpy as np

matrix = np.random.randint(20,100, size = (6,4))
print("Matrix:\n", matrix)

mean = np.mean(matrix, axis = 0)
print("Mean:\n", mean)

std = np.std(matrix, axis = 0)
print("Standard Deviation:\n", std)

brd = (matrix - mean) / std
print("Bridge:\n", brd)