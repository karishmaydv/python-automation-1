#constructor paramerter should be pass in class also with init const also
# self keyword is mandatory for calling varible names into method
#new keyword is not req to create the object

class Calculator:
    num = 10

    def __init__(self,a,b):
        self.firstnumber= a
        self.secondnumber= b  # here a and b are instance variable

        print("const will call automatically when obj created")

    def Summation(self):
        return self.firstnumber + self.secondnumber + Calculator.num


obj = Calculator(2,3)
obj.Summation()
print(obj.Summation())