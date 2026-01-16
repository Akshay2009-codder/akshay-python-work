class Person:
    num = 8

yash = Person()  #yash ek alag persion hai
rudra = Person() # rudr ek alag person hai

#lekin num ye ek class ki property hai rudr or yash dono ki

yash.name = "Yash"

# we can access number using any persion like rudr or it and we can it using class  but it change using class

yash.age = 20
yash.std = 3

rudra.name = "Rudra"
rudra.age = 30
rudra.std = 4
print(yash.__dict__)
print(rudra.__dict__) # dict function return data in dictinory

print(yash.name)
