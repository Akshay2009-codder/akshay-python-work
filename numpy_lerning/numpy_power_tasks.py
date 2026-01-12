import numpy as np

matrix = np.random.randint(10, 100, size=(4,3))
print("Matrix:\n", matrix)

# Task 1: Feature-wise mean & std
mean = np.mean(matrix, axis=0)
std  = np.std(matrix, axis=0)

print("Mean:", mean)
print("Std :", std)

normalized_data = (matrix - mean) / std
print("Normalized Data:\n", normalized_data)

# Task 2: Outlier detection & replacement
outliers = matrix > (mean + std)
matrix[outliers] = np.take(mean, np.where(outliers)[1])

print("Replaced Matrix:\n", matrix)
