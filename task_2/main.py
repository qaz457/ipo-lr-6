#1вариант
from random import randint,choice#импортируем методы с библиотеки 
numbers = [-3, -5, -2, -12, 0, 15, 4, 7, 2]#список чисел
height = randint(4,8)#рандомная высота
width =randint(4,8)#рандомная длина
sum = 0#сумма
num=[]#матрица
for i in range(height):#фор для длины матрицы
    arg = []#матрица 
    for j in range(width):#фор для ширины матрицы
        even = choice(numbers)#рандомное число с списка

        if even % 2 == 0:#проверка на четность
            sum += even#суммируем
        arg.append(even)#добавляем число в матрицу
    num.append(arg)#добавляем подматрицу в матрицу
    print(' '.join(f"{num:3}" for num in arg))#выводим по строчно матрицу
print(f"Сумма всех четных чисел - {sum}")#выводим сумму четных чисел