#try #exception
#try block will send req to except block if condtion failed
# we can use this in pop up handling and any other situation
#finally keyword will use only in try expt block
# finallay will exectue in any situtaion fail or correct every time will execute this
try:
    #with open('filelog.txt', 'r') as reader: # this file does not exist if this is not in try catchpython give error msg
     with open('test.txt', 'r') as reader: #this file is exist so try will execute
        reader.read()
except:
    print("some how i reached this block beacuse there is failure in try block")

try:
    with open('filelog.txt', 'r'):
        reader.read()
except  Exception as e:
    print(e) # referebce variable for actual exception
finally:
    print("cleaning up reasourses") # setup and teardown method can call if you want to delete cokkies this can use



