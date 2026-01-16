class Employee:
    def __init__(self, fname , lname):
        self.fname = fname
        self.lname = lname
        self.femail = f"{self.fname}.{self.lname}@ak.com"

    def explain(self):
      return f"Thish employee is {self.fname} {self.lname} "

    @property
    def email(self):
        return f"{self.fname}{self.lname}@ak.com"

    @email.setter
    def email(self, string):
     print("setting now...")
     names = string.split("@")[0]
     self.fname = names.split(".")[0]
     self.lname = names.split(".")[1]



yash_raj = Employee("Yash","desai" )
rudr_dev = Employee("Rudra","devda")

print(yash_raj.email)
yash_raj.fname = "Yashraj"
print(yash_raj.email)
yash_raj.email = "Akshay.dhumda@ak.com"
print(yash_raj.email)

print(id("i am Akshay Dhumda"))
# print(id("i am Akshay Dhumda"))
print(id("who is ak"))

# aage jo id likha hai vo iske use se ham ye kaha save hua hai uski id chack kar sakte hai