class Library:
    def __init__(self,name,author,year):
        self.name = name
        self.author = author
        self.year = year
    def display(self):
        print("Book name is : ",self.name)
        print("Writen by : ",self.author)
        print(f"written in {self.year}")
james = Library("Atomic habits",
                "James clear",
                "2018")
deep = Library("Deep work",
               "Cal Newport",
               "2016")
print("-------------")
print("book 1")
print("-------------")
deep.display()


print("-------------")
print("book 2")
print("-------------")
james.display()