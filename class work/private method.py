class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __getinfo(self):
        return f"name: {self.name}, salary: {self.salary}"

    def display(self):
        print(self.__getinfo())

emp_1 = Employee("Lucy", 5000)
emp_1.display()
