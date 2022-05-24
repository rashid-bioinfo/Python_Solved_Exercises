class CalcMethods:
    def __init__(self):
        print("Class ClacMethods is created")

    def add(self, num1, num2):
        self.num1 = self
        self.num2 = self
        return (self.num1 + self.num2)

# if __name__ == '__main__':
obj = CalcMethods()
ans = obj.add(3,4)
print (ans)