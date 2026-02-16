#every time open file make sure to close to prevent from corruption
# open the file location
# read n no characters by passing parameters
#readlines will pick list value and print using for loop

file = open('test.txt')
 # read all the content of file
#print(file.read())

# print few character
#print(file.read(2))
#file.close()

# read single line at a time or line by line
line = file.readline()
while line != "" :  # when line not blank this will execute
    print(line)
    line = file.readline()


print(file.readline())

#print line by line 100 by readline method


file.close()