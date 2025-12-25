def linear_search(list,key):
    for i in range (len(list)):
        if list[i] == key:
            return i
    return "not found"

print(linear_search([1,2,3,4,5],3))