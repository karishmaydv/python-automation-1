#class- user define blue print or prototype
#sum, multiplication, addition, constant method have to define
# class will have method, varisable, instance variable const etc.

class Calculator:   # calculator is function name
    num = 100   # varibales

    def getData(self):  # getdata method name
        print (" iam now executing as method in class")

obj = Calculator()  # syntax to create obj in  pyhton  no new operateor like java
# this will outside the class as starting from begining
obj.getData()  # method call
obj.num  # call the variable

