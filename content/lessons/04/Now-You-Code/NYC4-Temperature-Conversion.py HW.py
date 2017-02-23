temperature = int(input("enter a temperature: "))
unit = input("To which unit C or F: ")

if unit == "C":
    temperature = temperature * (9/5) + 32
    print("That's %f F" %temperature)

elif unit == "F":
    temperature = (temperature - 32) * (5/9)
    print("That's %f C" %temperature)
