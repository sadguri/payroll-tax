a = int(input('Введите вашу заработную плату:'))
if a<=20000:
    print(f'Вы освобождены от налога! Ваша зарплата составляет:{a}')
elif a>20000:
    b = a * 13 / 100
    b1 = a - b
    print(f'Ваша зарплата, после вычета налога в 13%, составит: {b1}')