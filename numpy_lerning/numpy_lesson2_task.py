import numpy as np

mat_1 = np.array([1,2,3,4,5,6])

print("Second element : " ,mat_1[1])
print("Last element : " ,mat_1[-1])
print("Middel element : " ,mat_1[2:4])

mat_2 = np.array([[1,2,66],[4,75,6],[7,89,9]])

print("First row : " ,mat_2[0,:])
print("Second column : " ,mat_2[1,:])
print("Grater then 50 values : " ,mat_2[mat_2>50])