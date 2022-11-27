# 3) Вводим с клавиатуры целое число - это зарплата.
# Нужно вывести в консоль -  Минимальное кол-во  купюр, которыми можно выдать ЗП.
# И сколько, и каких бухгалтер выдаст 25 рублевых купюр,  10 рублевых, 3 рублевых и 1 рублевых
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

def money_exchange(money): # 128
    count_25 = 0
    count_10 = 0
    count_3 = 0
    count_1 = 0
    print(f'При сумме {money}, размен будет:')
    while money > 0:
        if money // 25 > 0:
            count_25 += 1
            money -= 25
        elif money // 10 > 0:
            count_10 += 1
            money -= 10
        elif money // 3 > 0:
            count_3 += 1
            money -= 3
        elif money // 1 > 0:
            count_1 += 1
            money -= 1
    print(f'Купюры достоинством 25 рублей: {count_25} купюр \nКупюры достоинством 10 рублей: {count_10 } купюр \nКупюры достоинством 3 рубля: {count_3} купюр\nКупюры достоинством 1 рубля: {count_1} купюр')

money_exchange(get_number('Введите сумму: '))



