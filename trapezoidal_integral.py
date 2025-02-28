from math import sin
# --example--
# print(sin(0))
# >>> 0
# -----------
from math import pi

def integral(f,a=0,b=1,n=100):
    S=0
    h = (b - a)/n
    for i in range(1,n+1):
        S += h/2 * (f(a + (i-1)*h)+f(a+i*h))
    return (S)

result1 = integral(sin,0,pi/2,50)
print('(1){}'.format(result1))

def func2(x):
    return 4/(1+x**2)

result2 = integral(func2)
print('(2){}'.format(result2))

from math import sqrt
from math import exp
def func3(x):
    return sqrt(pi)*exp(-x)

result3 = integral(func3,-100,100,1000)
print('(3){}'.format(result3))


    









