names = ["Akshay", "Anil gandu", "Girish"]
roll_no = [7,23, 20]
marks =   [
    87, 90, 78,
    33, 13, 14,
    88, 77, 34,
]

class Student :
    def __init__(self, name, roll_no, marks1, marks2, marks3):

        self.name = name
        self.roll_no = roll_no
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3

    def display(self):
        Total = self.marks1 + self.marks2 + self.marks3
        Percent = Total/ 3
        print("Name     : ", self.name)
        print("Roll No  : ", self.roll_no)
        print("Marks    : ", self.marks1 , self.marks2 , self.marks3)
        print("Percent  : ", Percent)
        print("Total    : ", Total)

    def calculate(self):
        if self.marks1 >= 33 and self.marks2 >= 33 and self.marks3 >= 33:
            print("Result   : pass")
        else:
            print("Result   : fail")



student1 = Student(names[0],roll_no[0],marks[0],marks[1],marks[2])
print("_________________")
print(f"{names[0]} Report")
print("_________________")
student1.display()
student1.calculate()
print("\n")

student2 = Student(names[1],roll_no[1],marks[3],marks[4],marks[5])
print("_________________")
print(f"{names[1]} Report")
print("_________________")
student2.display()
student2.calculate()
print("\n")

student3 = Student(names[2],roll_no[2],marks[6],marks[7],marks[8])
print("_________________")
print(f"{names[2]} Report")
print("_________________")
student3.display()
student3.calculate()





