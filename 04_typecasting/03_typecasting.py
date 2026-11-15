# Typecasting - changing the data type of a variable into another is called TypeCasting . in python we can typecast a variable into another data type using the following functions :


# int() - converts a variable into an integer data type .
# float() - converts a variable into a float data type .
# str() - converts a variable into a string data type .
# bool() - converts a variable into a boolean data type .


a  = "109"

b = 13


print(a)
print(type(a)) # it is a string variable
print(b)
print(type(b)) # it is an integer variable


# convert string a into an integer 

c = int(a) # integer of a

print(type(c))
print(c) # it is an integer variable now

# convert flaot to intger 


pi = 3.14256
pi_int = int(pi)  # takes the integral value of the float
print(pi_int) 


# convert intger to boolean 

x = 10

y = bool(x)
print(y) # it will return True as long as number is not zero , for zero it will return false .
