# if- elif - else staements are nothing but long if else statements and its functions the same as if else statement 



age = int(input("enter the age:"))


if(age <0):
    print("you are not born yet")
elif(age > 0  and age <17 ):
    print("you are a minor")
elif(age>18 and age<100):
    print("you can vote")
else :                        # always put else at the end and not in between  and put elif in the between statements 
    print("you are dead")