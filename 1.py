dig = int(input("Введите целое число: "))
sysofcount = int(input("Выберете и введите двоичную или восьмиричную систему счисления: "))
if sysofcount != 2:
    if sysofcount != 8:  
        print("Некорректные данные, введите правильную систему счисления!")
if sysofcount == 2:
    b = ''
    while dig > 0:
        b = str(dig % 2 ) + b
        dig //= 2
    print("Искомое число равно: ", b)
elif sysofcount == 8:
    c = ''
    while dig > 0:
        c = str(dig % 8) + c
        dig //= 8
    print("Искомое число равно: ", c)

    
    
