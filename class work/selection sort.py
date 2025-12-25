def selection_sort(list):
    for i in range(len(list)):
       min_index = i
       for j in range(i+1,len(list)):
           if list[j] < list[min_index]:
                min_index = j
           list[i],list[min_index] = list[min_index],list[i]

    return list

print(selection_sort([5,4,3,2,1]))

