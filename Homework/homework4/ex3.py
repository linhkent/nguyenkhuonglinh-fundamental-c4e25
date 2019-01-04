print('''
Answer the following algebra question:
If x=8 then what is the value of 4(x+3)
1. 35
2. 36
3. 40
4. 44
''')
count = 1
check = int(input('Your choice: '))
while check != 4:
    check = int(input('Wrong! Choose other answer: '))
    count += 1
print('Bingo! Your try:',count,'time(s).')