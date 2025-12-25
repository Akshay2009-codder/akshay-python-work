class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

    @classmethod
    def display(cls):
      return  cls.count

s = Counter()
s2 = Counter()

print(Counter.display())

