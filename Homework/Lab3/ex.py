import turtle

# 1 Hello World
def hello_world():
    for i in range(3):
        print('Hello World!')

# 2 Sum
def add(x,y):
    print(x,'+',y,'=',x+y,sep='')

# 3 Draw square
def draw_square(l,c):
    turtle.color(c)
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(l)
        turtle.left(90)
    turtle.end_fill()

# 4 Check #3 (OK)
# for i in range(30):
#     draw_square(i * 5, 'red')
#     turtle.left(17)
#     turtle.penup()
#     turtle.forward(i * 2)
#     turtle.pendown()

# 5 Draw star
def draw_star(x,y,l):
    turtle.setposition(x,y)
    for i in range(5):
        turtle.right(144)
        turtle.forward(l)      

# 6 Check #5 (OK)
# turtle.speed(0)
# turtle.color('blue')
# for i in range(100):
#     import random
#     x = random.randint(-300, 300)
#     y = random.randint(-300, 300)
#     length = random.randint(3, 10)
#     draw_star(x, y, length) 
   
# 7 Remove $ sign
def remove_dollar_sign(s):
    s = s.replace('$','')
    return s

# 8 Check #7 (OK)
# string_with_no_dollars = remove_dollar_sign("$80% percent of $life is to show $up")
# if string_with_no_dollars == "80% percent of life is to show up":
#     print("Your function is correct")
# else:
#     print("Oops, there's a bug")

# 9 Get even list
def get_even_list(l):
    l1 = []
    for i in l:
        if i % 2 == 0:
            l1.append(i)
    return l1

# 10 Check #9 (OK)
# even_list = get_even_list([1, 2, 5, 9, -10, 6])
# if set(even_list) == set([2, -10, 6]):
#     print("Your function is correct")
# else:
#     print("Ooops, bugs detected")

# 11 Check side
def is_inside(s,p):
    check = True
    if p[0] > s[0] or p[1] > s[1]:
        check = False
    return check

# 12 Check #11 (OK)
# c1 = (is_inside([100,100],[90,90]))
# c2 = (is_inside([100,100],[110,110]))
# c3 = (is_inside([100,100],[110,90]))
# c4 = (is_inside([100,100],[90,110]))
# if c1 and (not c2) and (not c3) and (not c4):
#     print("Your function is correct")
# else:
#     print("Ooops, bugs detected")