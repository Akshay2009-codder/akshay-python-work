from functools import reduce


def sum_num(a,b):
    return a + b

liste_forex = [1,3,5,6,4]
list_sum = reduce(sum_num,liste_forex)
print(list_sum)
"""
koe pn list ma function apply karva mate list no upyog karvama aave che

"""
