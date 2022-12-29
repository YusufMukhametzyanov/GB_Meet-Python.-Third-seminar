# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]


list = [2, 3, 4, 5, 6]
new_list = []
count = len(list)
for i in range(len(list)):
    while len(new_list) < len(list) / 2 and count > len(list) / 2:
        count -= 1
        a = list[i] * list[count]
        i += 1
        new_list.append(a)
print(f"{list} => {new_list}")
