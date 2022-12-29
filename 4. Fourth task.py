# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

numbers = int(input("Enter number: "))
list = []
while numbers >= 1:
    a = numbers % 2
    numbers = int(numbers / 2)
    list.append(str(a))

count = len(list)
for i in range(len(list)):
    a = list[count - 1]
    list[count - 1] = list[i]
    list[i] = a
    count -= 1
    i += 1
    if count <= len(list) / 2: break

print(*list)