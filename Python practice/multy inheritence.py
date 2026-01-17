class Employee:
  number_of_employees = 10

  def __init__(self,name,roll,salary):
    self.name = name
    self.roll = roll
    self.salary = salary

  def print_employee_info(self):
    return f"the name is {self.name}, roll is {self.roll}, salary is {self.salary}"

  @classmethod
  def change_number_of_employees(cls,number_of_employee):
    cls.number_of_employees = number_of_employee

  @staticmethod
  def printing():
    print("Thank you Akshay dhumda")