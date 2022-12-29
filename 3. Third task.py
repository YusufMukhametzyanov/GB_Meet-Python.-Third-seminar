# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу
# между максимальным и минимальным значением дробной части элементов, отличной от 0.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

from random import uniform
number = int(input('Enter size list: '))
list = []
list2 = []

for i in range(number):
    list.append(round(uniform(0, 9), 2))

for i in range(len(list)):
    number_list2 = list[i] - int(list[i])
    list2.append(round(number_list2, 2))
print(f"{list} => {round(max(list2) - min(list2), 2)}")