def bainary_serch(lst,key):
    low,high = 0,len(lst)-1
    while low<=high:
        mid = (low+high)//2
        if lst[mid]==key:
            return mid
        elif lst[mid]>key:
            high = mid-1
        else:
            low = mid+1
    return "not found"

print(bainary_serch([1,2,3,4,5],5))