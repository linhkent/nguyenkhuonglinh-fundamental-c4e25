while True:
    import random
    x = random.randrange(0,50)
    y = random.randrange(0,50)
    ma = ['+','-','*','/']
    f = random.choice(ma)
    chx = ['y','n']
    ans = random.choice(chx)
    def true_ans(x,y,f):
        if f in ('+','-'):
            a = x + y
        else:
            a = x * y
        return(a)
    ques = true_ans(x,y,f)
    if ans == 'n':
        ques += random.choice([-2,-1,1,2])
    if f in ('+','*'):
        print(x,f,y,'=',ques,sep='')
    else:
        print(ques,f,x,'=',y,sep='')
    a = input('Yes or No (y/n) ').lower()
    pr = 'Wrong!'
    if a == ans:
        pr ='Yay!'
    print(pr)
# import calc
# print(calc.eval(7,8,'/'))