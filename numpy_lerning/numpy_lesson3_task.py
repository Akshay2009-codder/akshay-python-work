import numpy as np

matrix = np.random.randint(1,100, size = (4,3))
print(matrix)

column_sum = np.sum(matrix, axis = 0)
print("column vise sum : \n", column_sum)

mean_row = np.round(np.mean(matrix, axis=1),2)
print("mean row : \n", mean_row)

max_col = np.max(matrix, axis=0)
print("max col : \n", max_col)

min_row = np.min(matrix, axis=1)
print("min row : \n", min_row)
