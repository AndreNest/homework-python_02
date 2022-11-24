# 1) Вводим с клавиатуры целое число X и У.
# Выводим на экран количество чисел между Х и У, которые делятся на 2 и 3

def get_number(input_string):
    '''
    Проверка ввода на число.
    '''
    try:
        num = int(input(input_string))
        return  num
    except(ValueError):
        print('Ошибка ввода! Введите число!')
        return get_number(input_string)

def check_num(a,b):
    count = 0
    for i in range(a, b+1):
        if i % 2 == 0 and i % 3 == 0:
            count += 1
    print(f'Количество чисел подходящих под условия задачи - {count}')

check_num(get_number('Введите число X: '),get_number('Введите число Y: '))