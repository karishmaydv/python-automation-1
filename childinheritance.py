from constructorparameters import Calculator
# consturctor have to invoke on child constur from parent const
# cost declartion so inherit fromparent to child you need to call const in first step


class ChildImpl(Calculator):
    num2 = 200

    def __init__(self):
        Calculator.__init__(self,2,10)

    def getCompleteData(self): # method created
        return self.num2 + self.num + self.Summation()
    # to call method in class need to create obj
obj= ChildImpl()
print(obj.getCompleteData())

