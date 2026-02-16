# in list diff datatypes can allow in python
#list should be in [] square bracket
#it allow different data types with diff values
# we can inject values in list datatyp
#append will add new values in the list array


values = [1,2,"a",3, 4]

#print values in the index

print(values[0])
# it should be 1 from and array
# if you want to see the last index value in the list so
print(values[-1]) # 4
print(values[1:3]) # it will give index value  1 and 2 that means 2 and a

values.insert(3, "karishma")  # 3 par karishma replace hojayega
print(values)

values.append("yadav")  # it will add the value in end in array list
print(values)
# update values in list
values[2] = "A"
del values[0]
print(values)