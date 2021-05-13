class a_class:
    def __init__(self, number): 
        self.number = number


a = a_class(1)
print(a.number)
b = a
a = a_class(2)
print(a.number)
print(b.number)