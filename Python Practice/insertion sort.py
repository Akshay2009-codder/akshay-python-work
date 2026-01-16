def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i-1
        while j >= 0 and lst[j] > key:
            lst[j+1] = lst[j]
            j -= 1
            lst[j+1] = key
        lst[j+1] = key
    return lst
print(insertion_sort([1,3,6,8,6,4]))