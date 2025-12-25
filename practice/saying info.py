import pyttsx3

name = input("Enter your name: ")
age = input("Enter your age: ")
collage = input("Enter your collage: ")

about = (f"Hii {name}.i am a voice assistance, {name} you are {age} years old. and your callage is {collage}.Thankyou for chosing me.")
pyttsx3.speak(about)
print(about)