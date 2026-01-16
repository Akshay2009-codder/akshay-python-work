class School:
    def __init__(self, name, marks,roll_no):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def display(self):
     print("name    :", self.name)
     print("marks   : ",self.marks)
     print("roll_no : ",self.roll_no)

    def result(self):
        if self.marks >= 35:
            print("Result  : pass")
        else:
            print("Result  : fail")

student1 = School("Akshay", 80, "06")
student1.display()
student1.result()