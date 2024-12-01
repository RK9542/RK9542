num = int(input("Please enter a Number:"))
if (num > 0):
    if (num >0 and num < 10):
        print ("Number entered is between 0 to 10")
    elif (num >10 and num < 20):
        print ("Number is between 10 and 20")
    elif (num == 999):
        print ("Number is so specail")
    #else:
        #print ("Enter a valid number")
elif (num == 0):
    print ("Number entered is Zero")
else:
    print ("Number is Negative")