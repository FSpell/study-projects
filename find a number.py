from random import *
def request_yes_no():
    count = 0
    while True:
        a = input('Хотите сыграть еще раз? да/нет ')
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
        
def difficulty():
    count = 0
    while True:
        print('Выберите сложность 1-3')
        diff = input()
        if diff in ['1', '2', '3']:
            diff = int(diff)
            return diff
        else:
            if count > 2:
                print('Ок, выберу сам')
                diff = randrange(1, 4)
                return diff
            print('Попробуй еще -_-')
            count += 1
def is_valid(guess):
    valid_range = [str(i) for i in range(1, 100**diff + 1)]
    if guess in valid_range:
        return True
    else:
        return False
    
def game_round(diff):
    a = randrange(1, 100**diff + 1)
    print('Диапазон поиска 1 - ', 100**diff)
    count = 0
    while True:
        number = input('Введите число ')
        if not is_valid(number):
            print('А может быть все-таки введем целое число от 1 до ', 100**diff)
            continue
        number = int(number)
        count += 1
        if number < a:
            print('Ваше число меньше загаданного, попробуйте еще разок')
            continue
        elif number > a:
            print('Ваше число больше загаданного, попробуйте еще разок')
            continue
        elif number == a:
            print('Вы угадали, поздравляем!')
            if 2 <= count % 10 <= 4:
                print('Вы справились за ', count, 'попытки')
            elif count % 10 == 1:
                print('Вы справились за ', count, 'попытку')
            else:
                print('Вы справились за ', count, 'попыток')
            break

print('Добро пожаловать в числовую угадайку')
while True:
    diff = difficulty()
    game_round(diff)
    if request_yes_no():
        continue
    else:
        break
print('Спасибо, что играли в числовую угадайку. Еще увидимся...')

    
