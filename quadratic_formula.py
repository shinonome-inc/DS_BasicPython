a = 1
b = 0
c = 1

# TODO
x1 = (-b-(b**2-4*a*c)**0.5)/(2*a)
x2 = (-b+(b**2-4*a*c)**0.5)/(2*a)
if x1 != x2:
    print(x1,x2)
else:
    print(x1)
