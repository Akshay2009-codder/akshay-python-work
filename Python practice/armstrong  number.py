number = int(input("Enter a number for chacking armstrong number: "))
pw = len(str(number))
sum = 0
for digit in str(number):
    sum += int(digit)**pw
if sum == number:
    print("number is armstrong")
else:
    print("number is not armstrong")