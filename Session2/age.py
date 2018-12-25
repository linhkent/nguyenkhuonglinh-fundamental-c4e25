y = int(input("Year of birth: "))
age = 2018 - y
print(age)
if age < 10:
    print('baby')
elif age < 18:
    print('teenage')
else: 
    print('adult')