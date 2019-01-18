from random import *
global shapes
shapes = [
    {
        'text': 'blue',
        'color': '#3F51B5',
        'rect': [20, 60, 100, 100]
    },
    {
        'text': 'red',
        'color': '#C62828',
        'rect': [140, 60, 100, 100]
    },
    {
        'text': 'yellow',
        'color': '#FFD600',
        'rect': [20, 180, 100, 100]
    },
    {
        'text': 'green',
        'color': '#4CAF50',
        'rect': [140, 180, 100, 100]
    }
]
a = [1,2,3]
def is_inside(s,p):
    check = False
    if s[0] < p[0] < (s[0]+s[2]) and s[1]< p[1] < (s[1]+s[3]):
        check = True
    return check

def get_shapes():
    s = []
    for shape in shapes:
        s.append(shape)
    new_pos = []
    for i in range(len(s)):
        shape = choice(s)
        s.remove(shape)
        new_pos.append(shape['rect'])
    for  i, shape in enumerate(shapes):
        shape['rect'] = new_pos[i]
    return shapes

def generate_quiz():
    shape = choice(shapes)
    text = shape['text']
    shape = choice(shapes)
    color = shape['color']
    return [
                text,
                color,
                randint(0, 1) # 0 : meaning, 1: color
            ]

def mouse_press(x, y, text, color, quiz_type):
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

