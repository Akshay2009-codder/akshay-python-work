class Info:
    def __init__(self,name,number,email):
        self.name = name
        self.number = number
        self.email = email
    def display(self):
        print("name   : ",self.name)
        print("number : ",self.number)
        print("email  : ",self.email)
person1 =Info("Akshay",
              "7698737236",
              "akshaydhumda@gmail.com")
person1.display()