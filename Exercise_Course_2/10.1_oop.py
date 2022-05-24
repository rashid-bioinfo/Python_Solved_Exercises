'''
My first class creation
'''

class Number:
    def mysum(self):
        return self.a + self.b

num = Number() # Instantiate object of the class Number
num.a = 5
num.b = 7
c = num.mysum()
print(c)