import random
def generate_quiz():
    x = random.randrange(1,25)
    ma = ['+','-','*','/']
    op = random.choice(ma)
    if op in ('-','/'):
        y = random.randrange(3,25)
    else:
        y = random.randrange(1,25)
    chx = [True,False]
    ans = random.choice(chx)
    if op in ('+','-'):
        result = x + y
    else:
        result = x * y
    if op in ('+','*'):
        [a,b,re] = [x,y,result]
    else:
        [a,b,re] = [result,x,y]
    if ans == False:
        re += random.choice([-2,-1,1,2])
    # Hint: Return [x, y, op, result]
    return [a, b, op, re, ans]
def check_answer(ans, user_choice):
    sc = False
    if user_choice == ans:
        sc = True
    return(sc)
