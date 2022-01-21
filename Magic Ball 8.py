import time
import random
def taping_text(txt, delay):
    for i in txt:
        time.sleep(delay)
        print(i, end='', flush=True)
    print()
welcome = 'Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.'
taping_text(welcome, 0.03)
ask_name = 'Назови свое имя'
taping_text(ask_name, 0.03)
name = input()


def request_yes_no():
    count = 0
    while True:
        a = input('Остались вопросы? да / нет ')
        if a == 'да':
            return True
        elif a == 'нет':
            return False
        else:
            if count > 1:
                print('Нет вопросов, нет ответов...')
                return False            
            print('Непонимаю...')
            count += 1
            continue
def new_game():
    answers = ['Бесспорно', 'Мне кажется - да', 'Пока неясно, попробуй снова', 'Даже не думай',
    'Предрешено', 'Вероятнее всего', 'Спроси позже', 'Мой ответ - нет', 'Никаких сомнений', 'Хорошие перспективы', 'Лучше не рассказывать', 'По моим данным - нет', 'Определённо да', 'Знаки говорят - да', 'Сейчас нельзя предсказать', 'Перспективы не очень хорошие', 'Можешь быть уверен в этом', 'Да', 'Сконцентрируйся и спроси опять', 'Весьма сомнительно']
    print('Задай вопрос')
    question = input()
    txt = '...'
    taping_text(txt, 0.3)
    print()
    answer = random.choice(answers)
    print(answer)
while True:
    new_game()
    if request_yes_no():
        continue
    else:
        print('Возвращайся если возникнут вопросы!')
        break
    