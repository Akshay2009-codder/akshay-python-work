import bisect

number = 7

list_sorte = [1,3,4,6,9,22,31,56,78,89,90]

print (bisect.bisect_left(list_sorte,number))
bisect.insort(list_sorte,number)
print(list_sorte)

'''
bisect modul ek in  built pythone module hai ye module 
'''