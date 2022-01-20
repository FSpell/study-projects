from random import *
a = randrange(1, 101)
print('Welcome to fine a number game')
def is_valid(guess):
    valid_range=[i for i in range(1,101)]
    if guess in valid_range:
        return True
    else:
        return False
while True:
    number = input()
    if not is_valid:
        print('А может быть все-таки введем целое число от 1 до 100?')
        continue
    number = int(number)
    if number < a:
        print('Ваше число меньше загаданного, попробуйте еще разок')
        continue
    elif number > a:
        print('Ваше число больше загаданного, попробуйте еще разок')
        continue
    elif number == a:
        print('Вы угадали, поздравляем!')
        print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
        break


    
