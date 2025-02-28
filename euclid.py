a = input("a の値を入力: ")
b = input("b の値を入力: ")

# TODO
while b != 0:
        a,b = b, int(a) % int(b)
print('最大公約数：{}'.format(a)) 

    