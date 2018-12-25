# Converts Celsius (0C) into Fahrenheit (0F)
import os
kt = "y"
while kt == "y":
    os.system("cls") 
    dgc = int(input("Enter temperature of Celcius: "))
    while dgc < -273.15:
        dgc = int(input("Temperature must be greater than -273.15. Please enter temperature again: "))
    dgf = dgc*1.8+32
    print(dgc,"(C) = ",dgf,"(F)")
    kt = input("Again? (Y/N): ")
print("Thank you!")
# :D