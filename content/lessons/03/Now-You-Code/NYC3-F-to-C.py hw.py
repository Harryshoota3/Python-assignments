def distance():
    distance = float(input("Enter distance in feet:"))
    units = input("In which units yards or miles?")
    if units =="yards":
        distance = (distance*0.3333)
        print("That's",distance,"yards")
    elif units == "miles":
        distance == (distance*0.0001893940)
        print("That's",distance,"miles")
    else:
        print("The unit should be either yards or miles")

distance()
    
