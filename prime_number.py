a = input("aの値を入力: ")
b = input("bの値を入力: ")

# TODO
def check_natural(n):
    if not n.isdigit() or int(n)<0:
        raise ValueError('{}は自然数ではありません'.format(n))
check_natural(a)
check_natural(b)

def is_prime(n):
    if int(n) < 2:
        return False
    for i in range(2,int(n)):
        if int(n) % i == 0:
            return False
    return True

for x in [a,b]:
    if is_prime(x):
        print('{}は素数'.format(x))
    else:
        print('{}は素数ではない'.format(x))