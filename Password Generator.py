import random
def ask_question(text):
    print(text)
    answer = input()
    return(answer)

def removing_bad_symbols(txt):
    clear = []
    for i in range(len(txt)):
        if txt[i] not in 'il1Lo0O':
            clear.append(txt[i])
    return(clear)
def request_yes_no(txt):
    count = 0
    while True:
        a = input(txt+'\n')

        if a == 'да':
            return True
        elif a == 'нет':
            return False
        else:
            if count > 2:
                print('Cдаюсь, нам друг друга не понять, начинаю завершение работы...')
                return False            
            print('Непонимаю вас, повторите команду')
            count += 1
            continue


def safe_password_creator():
    digits = '0123456789'
    lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
    uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    punctuation = '#$%&*+-=?@^_'
    chars = ''
    while True:
        count = ask_question('Количество паролей для генерации? (от 1 до 10)')
        valid_range = [str(i) for i in range(1, 11)]
        if count in valid_range:
            count = int(count)
            break
        else:
            continue
    while True:
        lenght = ask_question('Длина одного пароля? от 3 до 20 символов')
        valid_range = [str(i) for i in range(1, 21)]
        if lenght in valid_range:
            lenght = int(lenght)
            break
        else:
            continue
    while True:
        need_digits = ask_question('Включать ли цифры 0123456789? да / нет')
        valid_range = ['да', 'нет']
        if need_digits in valid_range:
            if need_digits == 'да':
                need_digits = True
            else:
                need_digits = False
            break
        else:
            continue

    while True:
        need_big_letters = ask_question('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? да / нет')
        valid_range = ['да', 'нет']
        if need_big_letters in valid_range:
            if need_big_letters == 'да':
                need_big_letters = True
            else:
                need_big_letters = False
            break
        else:
            continue

    while True:
        need_small_letters = ask_question('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? да / нет')
        valid_range = ['да', 'нет']
        if need_small_letters in valid_range:
            if need_small_letters == 'да':
                need_small_letters = True
            else:
                need_small_letters = False
            break
        else:
            continue

    while True:
        need_symbols = ask_question('Включать ли символы !#$%&*+-=?@^_? да / нет')
        valid_range = ['да', 'нет']
        if need_symbols in valid_range:
            if need_symbols == 'да':
                need_symbols = True
            else:
                need_symbols = False
            break
        else:
            continue
    while True:
        easy_read = ask_question('Исключать ли неоднозначные символы il1Lo0O? да / нет')
        valid_range = ['да', 'нет']
        if easy_read in valid_range:
            if easy_read == 'да':
                easy_read = True
            else:
                easy_read = False
            break
        else:
            continue
    #count, lenght, need_digits, need_big_letters, need_small_letters, need_symbols,easy_read
    a = 0

    while a < count:
        chars = []
        while True:
            if need_digits:
                chars.append(random.choice(digits))
                if easy_read:
                    chars = removing_bad_symbols(chars)
                if len(chars) == lenght:
                    a += 1
                    break
            if need_big_letters:
                chars.append(random.choice(uppercase_letters))
                if easy_read:
                    chars = removing_bad_symbols(chars)
                if len(chars) == lenght:
                    a += 1
                    break
            if need_small_letters:
                chars.append(random.choice(lowercase_letters))
                if easy_read:
                    chars = removing_bad_symbols(chars)
                if len(chars) == lenght:
                    a += 1
                    break
            if need_symbols:
                chars.append(random.choice(punctuation))
                if easy_read:
                    chars = removing_bad_symbols(chars)
                if len(chars) == lenght:
                    a += 1
                    break
        random.shuffle(chars)
        result = ''.join(chars)
        print(result)
safe_password_creator()
while request_yes_no('Еще раз? да / нет'):
    safe_password_creator()
