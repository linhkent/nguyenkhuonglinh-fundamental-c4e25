a = float(input("a= "))
while a == 0:
    a = float(input("Nhap lai: "))
b = float(input("b= "))
c = float(input("c= "))
delta = b*b - 4*a*c
if delta < 0: 
    print ("Vo nghiem")
elif delta == 0:
    print ("Nghiem kep: ",-b/(2*a))
else:
    print ("N1 = ", (-b-(delta)**0.5)/(2*a))
    print ("N2 = ", (-b+(delta)**0.5)/(2*a))