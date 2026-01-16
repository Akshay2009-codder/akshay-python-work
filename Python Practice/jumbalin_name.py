students = int(input("How many students: "))
student = []

# input names
for i in range(students):
    k = input("Enter full name (first last): ")
    student.append(k)

first_names = []
last_names = []

for s in student:
    f, l = s.split()
    first_names.append(f)
    last_names.append(l)


jumbalin_name = []
for i in range(len(first_names)):
    jumbalin_name.append(first_names[i] + " " + last_names[(i+1) % len(last_names)])

print("\nJumbled Names:")
for name in jumbalin_name:
    print(name)
