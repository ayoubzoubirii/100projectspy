def calc ():
    print("Welecome to the tip calculator")
    total_bill = float(input("What was the total bill ?"))
    num_people = int(input("How many people to split the bill ?"))
    percentage = int(input("what percentage tip would like to give ? 10 , 12 or 15 ? "))
    if percentage == 10 : 
        pay = (percentage*(total_bill/100) + total_bill ) / num_people 
        print("Each person should pay :" + str(float(pay)))
    elif percentage == 12 : 
        pay = (percentage*(total_bill/100) + total_bill ) / num_people 
        print("Each person should pay :" + str(float(pay)))
    elif percentage == 15 : 
        pay = (percentage*(total_bill/100) + total_bill ) / num_people 
        print("Each person should pay :" + str(float(pay)))    
calc()