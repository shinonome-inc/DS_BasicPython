a = input("a の値を入力: ")
b = input("b の値を入力: ")

# TODO
def gcd(a,b):
    while b != 0:
        a,b = b, int(a) % int(b)
    return a 
result3 = gcd(a,b)
print(result3)

def coprime(a,b):
    while b != 0:
        a,b = b, int(a) % int(b)
    return a == 1

result4 = coprime(a,b)
if result4:
    print(f"{a}と{b}は互いに素")
else:
    print(f"{a}と{b}は互いに素ではない")
