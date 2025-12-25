def greter_2(n):
    if n > 2:
        return True
    else:
        return False

list_of_numbers = [1,2,3,-4,5,-6,7,8,-9]
greter_than_2 = list(filter(greter_2,list_of_numbers))
print(greter_than_2)

'''
aa filter function pn map function ni jem j kaam kare che'''




