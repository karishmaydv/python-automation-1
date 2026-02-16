# function - it is a grp of related statements that perform a specific task
# def is an identifier for function then will give fun name to define function
#pyhon in firs line : is used
# we have to follow code indentaion to start and end function or statement


#function declaration

def GreetMe():
  print("Good Morning")
  #function call
GreetMe()

# send parameter in function call

def GreetMe(name):
    print("Good Morning " + name) # + is used to concatenate
GreetMe("karishma yadav")

def AddIntegers(a,b):
    print(a+b)
AddIntegers(4,8)
