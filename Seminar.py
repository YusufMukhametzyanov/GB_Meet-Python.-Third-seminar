# my_list = [1, 2, 3, 4, 5]  # пример оформления листа в Python
# my_tuple = 1, 2, 3, '_', 5  # пример оформления кортежа в Python
# my_set = {1, 34, 535, 456, 4, 5} # множество
# my_lib = {(1, 2): '1', 'a': 555} # библиотека
# print(my_lib['a'])

my_list = ['fdsfdf', 'fdsfdsf', '34535', 'fafasdfd']
value = '45'
for i in range(len(my_list)):
    if value in my_list[i]:
        print(f'Значение {value} есть в {i} индексе')

