from random import *
global colors, rect
colors = [
    {
        'text': 'blue',
        'color': '#3F51B5',
    },
    {
        'text': 'red',
        'color': '#C62828',
    },
    {
        'text': 'yellow',
        'color': '#FFD600',
    },
    {
        'text': 'green',
        'color': '#4CAF50',
    },
    {
        'text': 'violet',
        'color': '#5D0C7B',
    },
    {
        'text': 'orange',
        'color': '#FF6600',
    },
    {
        'text': 'black',
        'color': '#000000',
    },
    {
        'text': 'gray',
        'color': '#A0A0A0',
    },
    {
        'text': 'pink',
        'color': '#FF33FF',
    },
]
rect = [
    [20, 60, 100, 100],
    [140, 60, 100, 100],
    [20, 180, 100, 100],
    [140, 180, 100, 100]
]
def is_inside(s,p):
    check = False
    if s[0] < p[0] < (s[0]+s[2]) and s[1]< p[1] < (s[1]+s[3]):
        check = True
    return check

def get_shapes():
    s = []
    shapes = []
    for c in colors:
        s.append(c)
    for i in range(4):
        shape = choice(s)
        s.remove(shape)
        shape['rect'] = rect[i]
        shapes.append(shape)
    return shapes

def generate_quiz(shapes):
    shape = choice(shapes)
    text = shape['text']
    shape = choice(shapes)
    color = shape['color']
    return [
                text,
                color,
                randint(0, 1) # 0 : meaning, 1: color
            ]

def mouse_press(x, y, text, color, quiz_type,shapes):
    if quiz_type == 0:
        for sh in shapes:
            if sh['text'] == text:
                shape = sh
    else:
        for sh in shapes:
            if sh['color'] == color:
                shape = sh
    check = is_inside(shape['rect'],[x,y])
    return check
