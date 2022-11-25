# 4) Вводим с клавиатуры многозначное число
# Необходимо узнать и сказать последовательность цифр этого числа при просмотре слева направо упорядочена по возрастанию или нет.
# Например 1579 - да ( 1 меньше 5, 5 меньше 7, а 7 меньше 9), 1427 - нет

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
def pars_num(num):
    arr = []
    i = 0
    while num > 0:
        arr.insert(0, num % 10)
        num = num // 10
    new_arr = sorted(arr)
    if new_arr == arr:
        print('Цифры идут по возрастанию!')
    else:
        print('Цифры идут не по возрастанию.')

def check_num(num_1):
    for i in range(len(num_1)):
        if num_1[i] > num_1[i - 1]:
            i += 1
            answer = "Цифры идут по возрастанию!"
        else:
            answer = "Цифры идут не по возрастанию."
    print(answer)


check_num(input('Введите число: '))
pars_num(get_number('Введите число X: '))



