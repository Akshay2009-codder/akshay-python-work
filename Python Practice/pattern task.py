num = int(input("Enter the number for print pettern : "))
tf = str(input(" if want reverse (y/n): "))

if tf=="n":
    for i in range(1,num+1):
        print("*" * i)
elif tf=="y":
    for i in range(num,0,-1):
       print("*" * i)
else:
  print("Please enter a valid input")