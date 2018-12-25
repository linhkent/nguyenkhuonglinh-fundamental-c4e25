import random
weather = random.randint(1,100)
if weather <= 30:
    print("rainy")
elif weather <= 60:
    print("clody")
else:
    print("sunny")
