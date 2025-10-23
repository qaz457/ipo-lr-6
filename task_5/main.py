#1 вариант
from random import randint#импортирую функцию randint
score_zero =0#создаю счетчик нулевых значений
score_pozitive =0#создаю счетчик положительных значений
score_negative =0#создаю счетчик отрицательных значений
random_number = [randint(-50,50) for i in range(25)]#генератор списка
for i in random_number:#прохожусть по списку
    if i == 0:#проверяю равно ли значение нулю
        score_zero += 1#добавляю 1 к счетчику
    elif i>0:#проверяю больше ли значение нуля
        score_pozitive += 1#добавляю 1 к счетчику
    else:#проверяю меньше ли значение нуля
        score_negative += 1#добавляю 1 к счетчику
print(random_number)#вывод списка
print(f'''Количсетво нулевых значений равно - {score_zero},в процентах это {score_zero/25*100}
Количсетво положительных значений равно - {score_pozitive},в процентах это {score_pozitive/25*100}
Количсетво отрицательных значений равно - {score_negative},в процентах это {score_negative/25*100}
Максимальное значение - {max(random_number)}
Минимальное значение - {min(random_number)}''')#вывод всей информации
