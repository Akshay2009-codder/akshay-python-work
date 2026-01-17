class employee:
    def __init__(self, name, salary,working_hours):
        self.__name = name
        self.__salary = salary
        self.__working_hours = working_hours

    def employee_details(self):
       return f"employee details: {self.__name}, {self.__salary}, {self.__working_hours}"

employee1 = employee("Raman", 2000, 50)

print(employee1.employee_details())