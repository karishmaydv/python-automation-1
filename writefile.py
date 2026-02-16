#read the file and store all lines in list
# reverse the list
# write the list back to the file

with open('test.txt','r') as reader: # file being open in read mode
    content = reader.readlines() # in list view read the output
    reversed(content)
    with open ('test.txt','w') as writer:
        for line in reversed(content):
            writer.write(line)