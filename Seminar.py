# my_list = [1, 2, 3, 4, 5]  # пример оформления листа в Python
# my_tuple = 1, 2, 3, '_', 5  # пример оформления кортежа в Python
# my_set = {1, 34, 535, 456, 4, 5} # множество
# my_lib = {(1, 2): '1', 'a': 555} # библиотека
# print(my_lib['a'])

# Задайте список. Напишите программу, которая определит, присутствует ли в заданном
# списке искомый элемент

# my_list = ['fdsfdf', 'fdsfdsf', '34535', 'fafasdfd']
# value = '45'
# for i in range(len(my_list)):
#     if value in my_list[i]:
#         print(f'Значение {value} есть в {i} индексе')

# Напишите программу, которая определит позицию второго вхождения
# строки в списке либо сообщит, что её нет

list1 = ['qwe', 'ewq', 123, 'asd', 123]
search_number = 123
count = 0
for i in range(len(list1)):
    if list1[i] == search_number:
        count += 1
        if count == 2:
            print(f'список: {list1}, ищем: "{search_number}", ответ: {i}')
if count == 0 or count == 1:
    print(f'список: {list1}, ищем: "{search_number}", ответ: -1')
