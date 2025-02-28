a = input("aの値を入力: ")
b = input("bの値を入力: ")

# TODO
for x in [a,b]:
    if int(x) < 2:
        print('{}は素数ではない'.format(x))
        continue

    is_prime = True
    for i in range(2,int(x)):
        if int(x) % i ==0:
            is_prime = False
            break
    
    if is_prime:
        print('{}は素数'.format(x))
    else:
        print('{}は素数ではない'.format(x))