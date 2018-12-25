def ttl():
    i = int(input("Shape you want to draw (1, 2): "))
    while i not in (1, 2):
        i = int(input("Invalid. Re-enter (1,2): "))
    if i == 1:
        color("red")
        left(22.5)
        for j in range(4):
            for k in range(2):
                left(135)
                forward (100)
                left(45)
                forward(100)
            left(90)
    else:
        m = int(input("Number of shape: "))
        for i in range (m):
            if i % 2 == 0:
                color("blue")
            else:
                color("red")
            for j in range (i+3):
                left(360/(i+3))
                forward(100)
    return()
def bmi(m,h):
    bmi = m/h/h
    if bmi < 16:
        stt = "severely underweight"
    elif bmi < 18.5:
        stt = "underweight"
    elif bmi < 25:
        stt = "normal"
    elif bmi < 30:
        stt = "overweight"
    else:
        stt = "obese"
    return (bmi,stt)

def fac(n):
    f = 1
    for i in range(n):
        f *= i+1
    return (f)
def ss(m,n):
    for i in range(n):
        for j in range(m):
            print("*", end = " ")
        print()
    return()
def sx(m,n):
    for i in range(n):
        for j in range(m):
            if (i+j) % 2 == 0:
                print("x", end = " ")
            else:
                print("*", end = " ")
        print()
    return()
kt = "y"
while kt == ("y" or "Y"):
    import os
    os.system("cls") 
    n0 = int(input('''What do you want: 
    1. Draw shape
    2. Calculate BMI
    3. Calculate factorial
    4. Draw stars pattern
    5. Draw stars and x pattern
    '''))
    while n0 not in (1,2,3,4,5):
        n0 = int(input("Invalid input. Re-enter: "))    
    if n0 == 1:
        from turtle import *
        ttl()
        mainloop()
    elif n0 == 2:
        m = float(input("Your weight: "))
        h = float(input("Your height: "))
        print("Your BMI is ",bmi(m,h)[0],". You are ",bmi(m,h)[1])
    elif n0 == 3:
        n = int(input("Enter n: "))
        print(n, end ="")
        print("!=",fac(n))
    else:
        m = int(input("Number of column: "))
        n = int(input("Number of row: "))
        if n0 == 4:
                ss(m,n)
        else:
                sx(m,n)
    kt = input("Again (Y/N): ")
print("Thank you!")



