# Calculate area of circle
import math
import os
kt = "y"
while kt == "y":
    os.system("cls") 
    r = int(input("Radius of circle: "))
    aa = r*r*math.pi
    print("Area: ",aa)
    kt = input("Again? (Y/N): ")
print("Thank you!")
# :D