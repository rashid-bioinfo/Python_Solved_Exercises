class Animals:
    pass

class Pets(Animals):
    pass

class Dog(Pets):
    
    def bark(self):
        print("bark bark")


d = Dog()
d.bark()
