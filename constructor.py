# in python construtor name should not be in class name.
#const call automatically when obj is created
# constructor - init keyword is used
# construct name will be init
#class varible is const instance  variable not






class Calculator:   # calculator is function name
    num = 100   #  class varibales
    def __init__(self):
        print(" iam automatically call when obj is created")

    def getData(self):  # getdata method name
        print (" iam now executing as method in class")

obj = Calculator()  # syntax to create obj in  pyhton  no new operateor like java
# this will outside the class as starting from begining
obj.getData()  # method call
obj.num  # call the variable
print(obj.num)


