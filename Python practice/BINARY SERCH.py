def bainary_serch(expression,key):
    low,high = 0,len(expression)-1
    while low<=high:
        mid = (low+high)//2
        if expression[mid]==key:
            return mid
        elif expression[mid]>key:
            high = mid-1
        else:
            low = mid+1
    return "not found"

print(bainary_serch([10,20,30,40,50,60,70],0))