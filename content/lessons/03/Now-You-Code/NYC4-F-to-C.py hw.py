def temp():
    temp = float(input("Enter temperature:"))
    units = input("In which units C or F?:")
    if units == "c":
        temp = ((9/5)*temp)+32
        print("That's",temp,"F")
    elif units == "F":
        temp = (temp-32)*(5/9)
        print("That's",tmp,"C")
    else:
        print("The unint should be wither C or F")

temp()
    
