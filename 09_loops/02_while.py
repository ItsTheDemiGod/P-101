# while loop is another type of loop used in python which is use to execute a block of code as long as the condition is true 

print(1)
print(2)
print(3)
print(4)
print(5)
print()

# syntax ---> While (condition) :
#               do something 
#               increase the couter variable (updation)
# if you dont increase the counter variable then the condition will always remain true and we will run into an infinite loop .



# print  1 - 5 using while loop 

i = 1
while (i<6):  # here we check the condition first out of everything the condition is checked first ,
    print(i)  # print 
    i+=1      # increase the counter variable (updation)



# infinite loops are 

while True :   # this is always true and 
    print('hello world') # this will turn into an infinite loop and it will keep keep on until your system crash 