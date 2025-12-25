class Employee:
  number_of_employees = 10

  def __init__(self,name,roll,salary):
    self.name = name
    self.roll = roll
    self.salary = salary

  def print_employee_info(self):
    return f"the name is {self.name}, roll is {self.roll}, salary is {self.salary}"

  @classmethod # aa class method puri class change kari sakay jem ke sadi method thi e function ma j changes thay che
  def change_number_of_employees(cls,number_of_employee):
    cls.number_of_employees = number_of_employee

  @staticmethod # static method no use pela ke last ma kai print karavva mate use thay che
  def printing():
    print("Thank you Akshay dhumda")

Yash = Employee("Yash", "student",100)
Rudra = Employee("Rudra", "programer",200,)

print(Yash.print_employee_info())
print(Rudra.print_employee_info())

class Player:
  number_of_games = 4

  def __init__(self,game,name):
    self.game = game
    self.name = name

  def print_game_info(self):
    return f"your name is {self.name}, and you playing+ game is {self.game}"

class Cool_programmer(Employee, Player):
   pass

Anas = Player(["cricket,free fire","football"],"Anas")



