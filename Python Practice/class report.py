class School:
    def __init__(self, name, roll_no, mark1, mark2, mark3):
        self.name = name
        self.roll_no = roll_no
        self.mark1 = mark1
        self.mark2 = mark2
        self.mark3 = mark3

    def display(self):
        total = (self.mark1 + self.mark2 + self.mark3)
        percent = ((self.mark1 + self.mark2 + self.mark3)) / 3
        print("Name        : " , self.name)
        print("Roll No     : " , self.roll_no)
        print("marks       : " , self.mark1, self.mark2, self.mark3)
        print("Total marks : " , total)
        print("Percentage  : " , percent)

    def calculate(self):
        if self.mark1 >= 30 and self.mark2 >= 30 and self.mark3 >= 30:
            print("Result      :  pass")
        else:
            print("Result      : fail")

Akshay = School ("Akshay", "07", 70, 90, 75)
Girish = School ("Girish", "06", 20, 80, 14)
print("------------")
print("Akshay Report")
print("_____________")
Akshay.display()
Akshay.calculate()
print("          ")
print("          ")
print("-------------")
print("Girish Report")
print("_____________")
Girish.display()
Girish.calculate()







