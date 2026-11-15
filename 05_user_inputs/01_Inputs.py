# in python we take user input using the input() function . it takes input from the user and returns it as a string data type . 
# input function always return string type data , so if we want to take input of any other data type we have to typecast it into that data type using the typecasting functions .


a = (input("enter the number: ")) # " prompt" is the message that will be displayed to the user when taking input . it is optional and can be omitted if not required but its not a good practies. 

print(a)
print(type(a))


# there are two ways by which we can type cast the input data 
# 1.  at the time of taking input
# 2. after taking the input we type cast it into the required data type .



# at the time of taking input

num = int(input("enter the number : "))
print(num)
print(type(num))



# after taking the input
num1  = input("enter the number : ")
num1 = int(num1)
print(num1)
print(type(num1)) 
