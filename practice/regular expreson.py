import re
from re import finditer

about_ak = '''Hello! My name is Akshay. I live in India, and my email is akshay123@example.com. 
You can also reach me at ak.tech99@gmail.com. 
I have 2 phone numbers: 9876543210 and 123-456-7890.
Today's date is 24-08-2025, and the time is 15:45.
Visit my website: https://akshaydev.in or http://example.org for more info.
Price list: apple=120, banana=50, orange=80.
Let's meet at 6:30 PM @ Café_99!
'''

# split function
print(f"spliting list : {about_ak.split('\n')}")

# re.serch function
print("\nre.serch ka example : ")
match = re.search(r'@example', about_ak)
if match:
    print("congratulation you goted it")
    print(match.group())
else:
    print("you cant got it")

# findall function ye jitni baar dia hue alimenthoga utne eliment ko list ke andar return karega
print(re.findall(r'2', about_ak))

# sub function
new_text = re.sub(r'email','akemail', about_ak)
print(new_text)


# finditer function ye current location dega uski
matches = re.finditer(r'.', about_ak)
# matches = re.finditer(r'^li', about_ak)
for matche in matches:
    print(f"{matche}")



