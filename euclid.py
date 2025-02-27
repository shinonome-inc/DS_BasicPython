a = input("a の値を入力: ")
b = input("b の値を入力: ")

# TODO
def euclid(x,y):
    while y != 0:
        x,y = y, int(x) % int(y)
    return(x)

result = euclid(a,b)
print('最大公約数：{}'.format(result))

    