answerFl = 'Нет'
answerTr = 'Да'
secret = 'Иди нахуй'
running = True

while running:
    question = input('Если Вадик не читает A Byte of Python, то он ебанашка? (пиши с большой буквы, мы же интелегенция) ')

    if question == answerTr:
        print('Молодец это правильный ответ!')
        running = False
    elif question == answerFl:
        print('Вадик, иди нахуй, ты тупой.')
    elif question == secret:
        print('Сам иди, чмо.')
else:
     print('Цикл завершен.')
