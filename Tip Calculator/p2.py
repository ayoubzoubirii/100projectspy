def calc ():
    print("Welecome to the tip calculator")
    total_bill = float(input("What was the total bill ?"))
    num_people = int(input("How many people to split the bill ?"))
    percentage = int(input("what percentage tip would like to give ?  "))  
    pay = (percentage*(total_bill/100) + total_bill ) / num_people 
    print("Each person should pay :" + str(round(float(pay),2)))    
calc()