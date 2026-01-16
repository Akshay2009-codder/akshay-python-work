from abc import ABC, abstractmethod, ABCMeta


class Shape (metaclass=ABCMeta):
    @abstractmethod
    def print_area(self):
        return 0

class Rectangle(Shape):

    def __init__(self, length, breath):
        self.length = length
        self.breath = breath

    def print_area(self):
        return self.length * self.breath

emp1 = Rectangle(8, 7)
print(emp1.print_area())

# ham direct abstract class ka object nahi bana sakte hain
