with open('currancyData.txt') as f:
    lines = f.readlines()

currencyDict = {}

for line in lines:
    parsed = line.strip().split()
    for item in parsed:
        try:
            rate = float(item)
            currencyDict[parsed[0]] = rate
            break
        except ValueError:
            continue

amount = float(input("Enter amount you would like to convert:\n"))
print("Available currency options:")
[print(item) for item in currencyDict.keys()]
currency = input("\nEnter the currency code you want to convert to:\n")
if currency in currencyDict:
    print(f"{amount} INR is equal to {amount * currencyDict[currency]} {currency}")
else:
    print("Invalid currency entered.")
