def eval(x,y,f):
    if f == '+':
        a = x + y
    elif f == '-':
        a = x - y
    elif f == '*':
        a = x * y
    elif f == '/':
        a = x / y
    else:
        a = 'Lỗi'
    return(a)
# x = int(input('Nhập x: '))
# y = int(input('Nhập y: '))
# f = input('Phép tính: ')
# if eval(x,y,f) != 'Lỗi':
#     print(x,f,y,'=',eval(x,y,f),sep='')
# else:
#     print(eval(x,y,f))

# def sayhi(name):
#     print('Hi')
#     print('Hi',name)
#     print('Bye')
# sayhi('Quân')
# sayhi('Nam')
# def add(x,y):
#     return x+y
# x = int(input('x= '))
# y = int(input('y= '))
# print (add(x,y))