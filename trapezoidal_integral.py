from math import sin
# --example--
# print(sin(0))
# >>> 0
# -----------
from math import pi
h = ( pi/2 - 0 ) / 100
S=0
for i in range(1,101):
    S += h/2 * (sin(0+(i-1)*h)+ sin(0+i*h))
print(S)
    



    









