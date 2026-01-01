def selection_sort(lst):
    n = len(lst)
    for i in range(n):
        min_index = i
        for j in range(i+1,n):
            if lst[j] < lst[min_index]:
                min_index = j
            lst[min_index],lst[i] = lst[i],lst[min_index]
    return lst

print(selection_sort([1,3,6,8,6,4]))