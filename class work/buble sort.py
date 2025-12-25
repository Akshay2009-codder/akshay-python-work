def buble_sort(list):
    for i in range(len(list)):
        for j in range(0,len(list)- i -1 ):
            if list[j] > list[j+1]:
                list[j],list[j+1] = list[j+1],list[j]
    return list

print(buble_sort([3,5,4,7,8,6,9]))