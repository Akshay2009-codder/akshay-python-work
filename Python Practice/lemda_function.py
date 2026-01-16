add = lambda x, y: x + y
print(add(100,1987))

'''
lamda ek temprory function che. jyare aapne moe function no upyog khali ek j vakhta karva ichta hoe tyare 
aapne la,da function no upyog kari sakie chie 
'''

'''
lamda function ka upyog list ko sort karne ke liye 
'''
def sorting_fun(val):
    return val[1]
list_num = [(1,6),(9,7),(33,74),(1,4),]
list_num.sort(key=sorting_fun)
print(list_num)