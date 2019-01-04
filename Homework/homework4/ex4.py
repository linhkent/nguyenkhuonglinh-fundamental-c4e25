print('''
Answer the following algebra question:
If x=8 then what is the value of 4(x+3)
1. 35
2. 36
3. 40
4. 44
''')
count = 0
check = int(input('Your choice: '))
if check == 4:
    print('Bingo!')
    count += 1
else:
    print(':(')
print('''
Estimate this answer (exact caculation is not needed):
Jack score these marks in 5 Math tests: 49, 81, 72, 66 and 52.
What is the mean?
1. 55
2. 65
3. 75
4. 85
''')
check = int(input('Your choice: '))
if check == 2:
    print('Bingo!')
    count += 1
else:
    print(':(')
print('------------------------------')
print('Your score: ',count,'/2',sep='')