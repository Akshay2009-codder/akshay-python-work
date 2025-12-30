import numpy as np

arr_2d = np.array([[1,2,3],[4,5,6],[7,8,9]])

"""
insert in to 2d array 
axis=1 - row vise 
axis=0 - column vise
"""

new_arr = np.insert(arr_2d,1,[2,6,4],axis=0)
print(new_arr)

new_ar = np.insert(arr_2d,3,[4,5,6],axis=1)
print(new_ar)