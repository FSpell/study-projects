def any_to_decimal(n, base):
    s = []
    s.extend(n)
    if base > 10:
        for i in range(len(s)):
            if s[i] in 'ZXCVBNMLKJHGFDSAQWERTYUIOP':
                s[i] = ord(s[i]) - ord('A') + 10
        for j in range(len(s)):
            if s[j] in 'zxcvbnmlkjhgfdsaqwertyuiop':
                s[j] = ord(s[j]) - ord('a') + 10
            
    count = 0
    summa = 0
    for i in range(len(s) - 1, -1, -1):
        summa += int(s[i]) * (base**count)
        count += 1
    return summa

def decimal_to_any(n, base):
    s = []

    while n >= base:
        a = n // base
        s.append(n % base)
        n = a
    s.append(n)
    if base > 10:
        for i in range(len(s)):
            if s[i] >=10 :
                s[i] = chr(s[i] + ord('A') - 10)

    s.reverse()

    return s

print('Приветствую. \n Это программа перевода чисел из одной системы счисления в другую')
while True:
    print('Программа поддерживает два режима:\n1 - Перевод из любой СС в десятичную\n2 - Перевод из десятичной СС в любую другую\nВыберите режим 1 / 2 ')
    mode = int(input())
    if mode == 1:
        base = int(input('Введите начальную СС\n'))
        n = input('Введите число\n')
        print(any_to_decimal(n, base))
        
    if mode == 2:
        base = int(input('Введите конечную СС\n'))
        n = int(input('Введите число\n'))
        print(*decimal_to_any(n, base), sep='')
    print('Еще раз? 1 - да, 2 - нет')
    yesno = int(input())
    if yesno == 1:
        continue
    else:
        break










