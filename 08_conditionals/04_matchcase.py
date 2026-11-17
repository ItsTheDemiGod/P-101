# match cases are just like if else staements but rather than go thourgh a series of conditions we simply check which case matches with our input we do the desired action



# day = input("enter the day of the week")
day = input("enter the day of the week :")



match day:     # how this works is the value of day is matcher with all the cases and the one which matches its block of code is executed
    case "sunday":
        print("its sunday")
    case "monday":
        print("it is monday")
    case "tuesday":
        print("its tuesday")
    case "wednesday":
            print("wednesday")
    case "thursday":
          print("thursday")
    case "friday":
          print("its friday")
    case "saturday":
          print("its satuday")
    case _:
          print("not a valid day")




