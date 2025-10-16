#1вариант
from random import randint,choice
numbers = [-3, -5, -2, -12, 0, 15, 4, 7, 2]
height = randint(4,8)
width =randint(4,8)
sum = 0
num=[]
for i in range(height):
    arg = []
    for j in range(width):
        even = choice(numbers)

        if even % 2 == 0:
            sum += even
        arg.append(even)
    num.append(arg)
    print(' '.join(map(str,num[i])))
print(f"Сумма всех четных чисел - {sum}")