import func_class as fc

class CalcInterface:
    def __init__(self):
        print("CalcInterface class is created")

    # def inputNumber(self):
    #     num1 = int(input("Please enter a number: "))
    #     num2 = int(input("Please enter a number: "))
        # print(num1+num2)

    num1 = int(input("Please enter a number: "))
    num2 = int(input("Please enter a number: "))

objMain = CalcInterface()
# objMain.inputNumber()
objmethods = fc.CalcMethods()

ans = fc.add(objMain.num1, objMain.num2)
# ans = objmethods.add(num1, num2)

# print(ans)