def liniar_serch(lst,key):
    for i in range (len(lst)):
        if lst[i] == key:
            return i
    return -1

print(liniar_serch([1,2,5,7,8,5,7,9],7))