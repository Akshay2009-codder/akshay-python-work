import random
from random import choices

print("\n\nWelocome to snack, gun, water game")
print("\n===================================\n")
while True:

  print("press q to quit")
  you = str(input("Enter your choice (snack, gun, water) : "))
  if you == "q":
      break
  else:


   option = ["snack", "gun", "water"]
   pc = random.choice(option)

   if pc == "snack" and you == "water" or pc == "water" and you == "gun" or pc == "gun" and you == "snack":
     print("you lose , try again\n")
   elif pc == "water" and you == "snack" or pc == "gun" and you == "water" or pc == "snack" and you == "gun":
     print("you win\n")
   elif pc == you:
    print("game was tye\n")
   else:
      print("please give valid input")


print("\nThank you for playing")

print("\n========================================")