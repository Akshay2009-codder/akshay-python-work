names = ["Akshay", "yash", "Priyanshi"]
roll_no = [7, 23, 20]
marks = [
    87, 90, 78,     # Akshay
    63, 73, 43,     # Yash
    88, 77, 34      # Priyanshi
]

class Student:
    def __init__(self, name, roll_no, mark1, mark2, mark3):
        self.name = name
        self.roll_no = roll_no
        self.mark1 = mark1
        self.mark2 = mark2
        self.mark3 = mark3
        self.total = mark1 + mark2 + mark3
        self.percent = self.total / 3

    def display(self):
        print("Name     : ", self.name)
        print("Roll No. : ", self.roll_no)
        print("Percent  : ", self.percent)
        print("Total    : ", self.total)

    def calculate(self):
        if self.mark1 >= 33 and self.mark2 >= 33 and self.mark3 >= 33:
            print("Result   : Pass")
        else:
            print("Result   : Fail")

# Creating objects
student1 = Student(names[0], roll_no[0], marks[0], marks[1], marks[2])
student2 = Student(names[1], roll_no[1], marks[3], marks[4], marks[5])
student3 = Student(names[2], roll_no[2], marks[6], marks[7], marks[8])

# Bas ranking wala part rakho
students = [student1, student2, student3]
student_sorting = sorted(students, key=lambda x: x.total, reverse=True)

for idx, s in enumerate(student_sorting, start=1):
    print(f"Rank {idx} 🏅")
    s.display()
    s.calculate()
    print("--------------------------")