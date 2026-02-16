str = "RahulShettyAcademy.com"
str1 = "consulting firm"
str3 = "RahulShetty"

print (str[1])  # a will print start with o
print(str[0:5])# it will print r to l 0 to 4  python it start from o to n-1 . this is substring
print (str + str1)# to concatenation
print(str3 in str ) # in str str 3 string is present or not # sustring check

str.split(".") # str will break from .
var = str.split(".")
print(var)
print(var[0]) # it will print first part o index
str4 = " great "
print(str4.strip()) # this will shift the white space
print(str4.lstrip()) # it will shift whitespace left
print(str4.rstrip())  # it shift  whitespace right