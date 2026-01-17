item = {"vadapav": 30,
        "dabeli" : 35,
        "puf"    : 40}


class hotel_system:
    def __init__(self):
        pass

    def menu(self):
        print("Welcome to the hotel system!")
        for v in item:
            print(f"{v} - {item[v]}")
        order = input("What do you want to order? ")
    def provide(self):
        if order =="vadapav":
            print("vadapav reddy")


