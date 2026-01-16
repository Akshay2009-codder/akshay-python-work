# num1 = int(input("Enter first number for chack pelindrom : "))
# num2 = int(input("Enter second number for chack pelindrom : "))
# num3 = int(input("Enter third number for chack pelindrom : "))
#
# n = num1 + 1000
# for i in range(num1,n):
#     if str(num1) == str(num1)[::-1]:
#         print("you entered number is pelindrom",num1)
#         break
#     else:
#      if str(i) == str(i)[::-1]:
#         print(f"your next pelindrom for {num1} is {i}")
#         break
#
# for i in range(num2,n):
#     if str(num2) == str(num2)[::-1]:
#         print("you entered number is pelindrom",num2)
#         break
#     else:
#      if str(i) == str(i)[::-1]:
#         print(f"your next pelindrom for {num2} is {i}")
#         break
#
#
# for i in range(num3,n):
#     if str(num3) == str(num3)[::-1]:
#         print("you entered number is pelindrom",num3)
#         break
#     else:
#      if str(i) == str(i)[::-1]:
#         print(f"your next pelindrom for {num3} is {i}")
#         break
#
# print("Your pelindroms are fond sucessfully")

num1 = int(input("Enter first number for chack pelindrom : "))
num2 = int(input("Enter second number for chack pelindrom : "))
num3 = int(input("Enter third number for chack pelindrom : "))

def  next_pelindrom(num):
     n = num + 1000
     if str(num) == str(num)[::-1]:
      print("your number is pelindrom ",num)
     else:
      for i in range(num,n):
         if str(i) == str(i)[::-1]:
             print(f"your next pelindrom for {num} is {i}")
             break
next_pelindrom(num1)
next_pelindrom(num2)
next_pelindrom(num3)


