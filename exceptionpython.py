

ItemsInCart = 0
# 2 items will be addded to cart
# only 1 product is added in cart in that case
# will addthe expyion and tc will fail and this msg will display.
#assertion is one way of condition if not it will failed
# assert condtion fail will give failure tc  and it break when condtion not met.

if ItemsInCart !=  2:
    # raise Exception ("Products Cart count not matching")
    pass
#assert(ItemsInCart == 2)  #will give error because cart 0 item is matched

assert(ItemsInCart ==0)  #not give error

# try and except expetion is used- if the try condtion is failed it will go to the except block and print
# if try  condtion tre and exist

