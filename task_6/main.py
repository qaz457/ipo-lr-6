#1 ВАРИАНТ
from random import randint#импортируем функцию для случайног очисла
from itertools import combinations#исспортируем функцию для нахождения уникальных пар

random_number = [tuple(randint(-10, 10) for i in range(4)) for j in range(20)]#создаем список изх 20 значений по 4 числа
print("Исходный список (20 элементов по 4 числа):")#выводим текст
for i, row in enumerate(random_number, 1):#проходимся по списку
    print(f"{i}: {row}")#выводим по строчно

unique_combinations = list({tuple(sorted(row)) for row in random_number})#находим все уникальные  комбинации
print("Уникальные комбинации (порядок не учитывается):")#выводим текст
for combo in unique_combinations:#проходимя по уникальным комбинациям
    print(combo)#вывод их


n = int(input("Введите целое число: "))#запрашиваем число

count = 0#создаем счетчик
pairs = list(combinations(unique_combinations, 2))#создаем список из 2 уникальных комбинации

for a, b in pairs:#проходимя по этим парама
    if sum(a) + sum(b) < n:#проверяем меньше ли их сумма n
        count += 1#плюс один к счетчику

print(f"Количество пар, сумма которых меньше {n}: {count}")#выводим сколько пар меньеше чем n
#
