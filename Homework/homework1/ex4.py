sp = input("Choose the shape you want to draw (Square: S, Triangle: T, Circle: C): ")
while sp not in ("S", "T", "C", "s", "t", "c"):
    sp = input("Invalid input. Please enter one of word: S, T, C: ")
n = int(input("Enter number of shape: "))
dg = 360/n
from turtle import *
color("blue", "yellow")
begin_fill()
if sp in ("S", "s"):
    for i in range(n):
        for j in range (4):
            forward(100)
            left(90)
        left(dg)
elif sp in ("T", "t"):
    for i in range(n):
        for j in range (3):
            forward(100)
            left(120)
        left(dg)
else:
    for i in range(n):
        circle(100)
        left(dg)
end_fill()
mainloop()