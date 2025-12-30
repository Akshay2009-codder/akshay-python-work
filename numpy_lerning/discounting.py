import numpy as np

values = np.array([100,200,300,400])
discount = 10

final_price = values - values * discount/100
print(final_price)