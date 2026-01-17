class Employee:
    no_of_lives = 8

    def __init__(self, name ,sallary, role):
        self.name = name
        self.sallary = sallary
        self.role = role

    def print_details(self):
        return f"hellow {self.name} your sallary is {self.sallary} and your role is {self.role}"

    def __add__(self, other):
        return self.sallary + other.sallary
    # ye ek special method hai jo hame operator overloading karne me hlp karta hai



    def __truediv__(self, other):
        return self.sallary / other.sallary
    #ye method divison ke liye kaam aata hai

    def __repr__(self):
        return f"Employee({self.name}, {self.sallary}, {self.role})"

    def __str__(self):
        return "I am str methode i colled first "

emp1 = Employee("ysh",444, "codder")
print(repr(emp1))

# agar ham repr lagakar call karenge to hi repr method run karega varna pahle str hi karega

# emp2 = Employee("rudra",11, "clener")
# print(emp1 / emp2)

