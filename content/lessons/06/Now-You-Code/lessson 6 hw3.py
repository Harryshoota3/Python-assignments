import math

def calc_area(radius):
    try:
        area = radius * radius * math.pi
        return area
    except ValueError:
        print ("INVALID RADIUS")

def calc_circ(radius):
    try:
        circumference = 2 * math.pi * radius
        return circumference
    except ValueError:
        print ("INVALID RADIUS")


rad = int(input("Enter Circle Radius: "))
area = calc_area(rad)
circumference = calc_circ(rad)
print("A circle with radius %f has a Circumference of %f and an Area of %d" %(rad, circumference, area))
          
