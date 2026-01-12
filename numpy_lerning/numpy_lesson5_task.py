import numpy as np

arr = np.random.randint(1, 55, size = (3,3))
print("Array : \n",arr)

arr_2 = np.array([4,6,9])
print("Array 2 : \n",arr_2)

adding = arr + arr_2
print("Array addition : \n",adding)

multiple = adding * 2
print("Array multiplication : \n",multiple)

sqrt_calculation = np.round(np.sqrt(arr),2)
print("Array sqrt calculation : \n",sqrt_calculation)

print("Shape : ",np.shape(adding))