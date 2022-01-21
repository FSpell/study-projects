def rus_cod(s, n):
    result = ''
    for i in range(len(s)):
        if ord('а') <= ord(s[i]) <= ord('я'):
            etap1 = ord(s[i]) + n
            if etap1 > ord('я'):
                etap1 = etap1 - 32
            if etap1 < ord('а'):
                etap1 = etap1 + 32
                
            result += chr(etap1)
        elif ord('А') <= ord(s[i]) <= ord('Я'):
            etap1 = ord(s[i]) + n
            if etap1 > ord('Я'):
                etap1 = etap1 - 32
            if etap1 < ord('А'):
                etap1 = etap1 + 32
    
            result += chr(etap1)
        else:
            result += (s[i])
    return result
def eng_cod(s, n):
    result = ''
    for i in range(len(s)):
        if ord('a') <= ord(s[i]) <= ord('z'):
            etap1 = ord(s[i]) + n
            if etap1 > ord('z'):
                etap1 = etap1 - 26
            if etap1 < ord('a'):
                etap1 = etap1 + 26
            result += chr(etap1)
        elif ord('A') <= ord(s[i]) <= ord('Z'):
            etap1 = ord(s[i]) + n
            if etap1 > ord('Z'):
                etap1 = etap1 - 26
            if etap1 < ord('A'):
                etap1 = etap1 + 26
            result += chr(etap1)
        else:
            result += (s[i])
    return result
def is_valid(guess):
    valid_range = ['1','2']
    if guess in valid_range:
        return True
    else:
        return False
def get_info():
    while True:
        print('Выберите действие:\n1 - шифровать\n2 - дешифровать')
        way = input()
        if not is_valid(way):
            print('ошибка')
            continue
        way = int(way)
        break
    while True:
        print('Выберите язык:\n1 - английский\n2 - русский')
        lang = input()
        if not is_valid(lang):
            print('ошибка')
            continue
        lang = int(lang)
        break
    while True:
        print('Выберите шаг сдвига')
        step = input()
        if not step.isdigit():
            print('ошибка')
            continue
        step = int(step)
        break

    if lang == 1:
        step = step % 26
    elif lang == 2:
        step = step % 32
    return way, lang, step
def request_yes_no():
    count = 0
    while True:
        a = input('Еще раз?\n1 - да \n2 - нет\n')
        if a == '1':
            return True
        elif a == '2':
            return False
        else:
            if count > 2:
                print('Cдаюсь, нам друг друга не понять, начинаю завершение работы...')
                return False            
            print('Непонимаю вас, повторите команду')
            count += 1
            continue

print('Шифр цезаря')
while True:
    way, lang, step = get_info()
    txt = input('Введите текст: \n')
    if way == 2:
        step = -1 * step
    if lang == 1:
        print(eng_cod(txt, step))
    if lang == 2:
        print(rus_cod(txt, step))
        print()
    if request_yes_no():
        continue
    else:
        break
