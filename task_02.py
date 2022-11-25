# 2) Вводим с клавиатуры целое число X
# Далее вводим Х целых чисел.
# Необходимо вывести на экран максимальное и второе максимальное число из введенных чисел.
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
def max_num(x):
    arr = []
    for i in range(x):
        num = arr.append(get_number('Введите число Х: '))

    arr.sort()
    print(f'Первое максимальное число: {arr[-1]}, Второе максимальное число: {arr[-2]}')

max_num(get_number('Сколько числе будет введено? '))


