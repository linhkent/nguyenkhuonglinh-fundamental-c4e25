def ex1(turtle):
# Turtle excercises
    colors = ['red', 'blue', 'brown', 'yellow', 'grey']
    choice = input('''What shape do you want to draw: 
    1. Polygons
    2. Flags
    ''')
    # turtle.reset()
    turtle.speed(10)
    while choice not in ("1","2"):
        choice = input("Invalid input. Please enter (1) or (2): ")
    if choice == "1":
        for i in range(5):
            turtle.color(colors[i])
            for j in range (i+3):
                    turtle.left(360/(i+3))
                    turtle.forward(100)
    else:
        turtle.penup()
        for i in range(5):
            turtle.color(colors[i])
            turtle.begin_fill()
            for j in range(2):
                turtle.forward(50)
                turtle.left(90)
                turtle.forward(100)
                turtle.left(90)
            turtle.end_fill()
            turtle.setposition(50*i+50,0)
    return()
def ex2():
# Manage clothes shop
    items = ['T-Shirt', 'Sweater']
    chx = input('''What do you want:
    1. Add new cloth (C)
    2. Update new cloth (U)
    3. Delete one cloth (D)
    4. Exit (E)
    ''')
    print ("Our shop have: ", items)
    while chx not in ('C', 'U', 'D', 'E','c','u','d','e'):
        chx = input("Invalid input. Please re-enter (C, U, D, E): ")
    while chx not in ('E', 'e'):
        if chx in ('C', 'c'):
            items.append(input("Enter name of new cloth: "))
        elif chx in ('U', 'u'):
            p = int(input("Select cloth's position you want to update: "))
            items[p-1] = input("New items: ")
        else:
            p = int(input("Select cloth's position you want to delete: "))
            del items[p-1]
        print ("Our shop have: ", items)
        chx = input("Any thing else?(C, U, D, E):")
        while chx not in ('C', 'U', 'D', 'E','c','u','d','e'):
            chx = input("Invalid input. Please re-enter (C, U, D, E): ")
    print ("Goodbye!")
    return()
def ex3():
# Shear the sheep
    flock = []
    nm = input("Enter your name: ")
    n = int(input("Enter number of sheep the flock: "))
    for i in range(n):
        print ("Size of the sheep",i+1,":")
        flock.append(int(input()))
    print ("-----------------------------------------")
    m = int(input("How many month do you want to work? "))
    print ("My name is",nm,". And here is my flock: ")
    print (flock)
    print ("-----------------------------------------")
    print ("Month 0:")
    print ("--------")
    print ("Now my biggest sheep has size", max(flock), ". Let's shear it")
    print ("After shearing, hear is my flock: ")
    flock[flock.index(max(flock))] = 8
    print (flock)
    print ("-----------------------------------------")
    for i in range(m):
        print ("Month",i+1,":")
        print ("--------")
        print ("One month passed.")
        print ("My sheep have grown. Here is my flock: ")
        for i in range(n):
            flock[i] += 50
        print (flock)
        print ("Now my biggest sheep has size", max(flock), ". Let's shear it")
        print ("After shearing, hear is my flock: ")
        print (flock)
        flock[flock.index(max(flock))] = 8
        print ("-----------------------------------------")
    return()
def ex4():
# word jumble
    kt4 = "Y"
    while kt4 in ("Y","y"):
        print ("Let's play word jumble")
        print ("Guess my word")
        print ("You have a clue")
        seq = []
        chaos = []
        words = ['champion', 'hexagon', 'meticulous','olympia','victory','forbidden','diamond','dragon']
        n = random.randrange(0,len(words))
        w = words[n]
        l = len(w)
        for i in range(l):
            seq.append(i)
        for i in range(l):
            j = random.randrange(0,len(seq))        
            print (w[seq[j]], end = " ")
            del seq[j]
        print()
        ws = input("Your answer is: ")
        while ws != w:
            ws = input("Wrong! Try again: ")
        print("Hura! You are fabulous!")
        kt4 = input("Wanna play again? (Y/N): ")
    return()
# Main:
kt = "y"
while kt == ("y" or "Y"):
    import os
    os.system("cls") 
    n0 = int(input('''What do you want: 
    1. Draw shape
    2. Manage clothes shop
    3. Shear the sheep
    4. Play word jumble
    '''))
    while n0 not in (1,2,3,4):
        n0 = int(input("Invalid input. Re-enter: "))    
    if n0 == 1:
        import turtle
        sc = turtle.TurtleScreen()
        t = turtle.Turtle()
        ex1(t)
        
        #sc = t.getscreen()
        #sc.onclick("stop")
    elif n0 == 2:
        ex2()
    elif n0 == 3:
        ex3()
    else:
        import random
        ex4()
    kt = input("Again (Y/N): ")
print("Thank you!")






    

                
