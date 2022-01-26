import random
#'ПРИВЕТ', 'СЛОВО
word_list = ['МАМА', 'ОТЕЦ', 'ДОЧЬ', 'КОМПЬЮТЕР', 'ЗЕРКАЛО', 'СТОЛ', 'ЛЕКАРСТВО', 'ФИЛЬМ', 'СЕРИАЛ', 'ОДЕЯЛО', 'КВАРТИРА', 'ХОЛОДИЛЬНИК', 'ПРОЕКТОР', 'КУХНЯ', 'СПАЛЬНЯ', 'ГОСТИННАЯ', 'ЭКРАН', 'ДЕРЕВО', 'ЛЕС', 'СТАНОК', 'КОМОД', 'МЕЛЬНИЦА', 'ТЕЛЕФОН', 'ШАПКА']
def get_word():
    return random.choice(word_list)
word = get_word()
def play(word):
    guessed = False
    word_completion_list = ['_' for i in range(len(word))]
    word_list = [i for i in word]
    guessed_letters = []
    guessed_words = []
    tries = 12
    print('Давайте играть в угадайку слов!')
    print('Осталось попыток:', tries)
    while True:
        print(*word_completion_list)
        if tries == 0:
            print('Вы проиграли')
            break
        a = input('Введите букву или слово целиком\n')
        a = a.upper()
        a = a.strip()
        if a in guessed_letters:
            print('Вы уже называли эту букву')
            continue
        if a in guessed_words:
            print('Вы уже называли это слово, и оно неверное Ха-Ха-Ха')
            
        if len(a) == len(word):
            guessed_words.append(a)
            if a == word:
                print('Вы выиграли')
                break
            if a != word:
                print('Неверно, попробуй еще')
                tries -= 1
                print('Осталось попыток:', tries)

        elif len(a) == 1:
            guessed_letters.append(a)
            if a in word:
                print('Верно!')
                for i in range(len(word_list)):
                    if a == word_list[i]:
                        word_completion_list[i] = a
                print(*word_completion_list)
            if '_' not in word_completion_list:
                print('Вы выиграли')

                break

            if a not in word:
                print('Неверно!')
                tries -= 1
                print('Осталось попыток:', tries)
                continue
            
        elif len(a) > 1:
            print('Ошибка, угадывай по 1 букве либо назови слово сразу.')
            continue
        
flag = True
while flag == True:
    play(get_word())
    while True:
        yesno = input('Хотите сыграть еще?\n1 - Да\n2 - Нет\n')
        if yesno == '1' or yesno == 'да':
            flag = True
            break
        elif yesno == '2' or yesno == 'нет':
            flag = False
            break
        else:
            print('Ошибка')
            continue
print('Спасибо за игру! До новых встреч!')