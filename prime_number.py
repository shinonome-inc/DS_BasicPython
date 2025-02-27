a = input("aの値を入力: ")
b = input("bの値を入力: ")

# TODO
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