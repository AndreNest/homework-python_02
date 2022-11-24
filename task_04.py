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
    while num > 0:
        arr.insert(0, num % 10)
        num = num // 10
    print(arr)
    return arr

def compar_num(arr):
    for i in arr:
        min_num = arr[0]
        if arr[i+1] > min_num:
            min_num = arr[i+1]
            print('ok')
        else:
            print('herny')
    print(f' min {min_num},index {i}')

# min_num = arr[i]

compar_num(pars_num(get_number('Введите число X: ')))



