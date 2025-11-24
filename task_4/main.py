#1 вариант
input_string = input("Введите строку для поиска:")#запрашивем строку для поиска

matched = []#создаем лист для совпадений
with open("text.txt",'r',encoding='utf-8') as file:#открываем файл для чтения

    for line in file:#проходимся по каждой строке файла
        if input_string in line:#проверйем на вхождение
            matched.append(line)#добавляем  в наш лист совпадений

print(f'Найдено строк - {len(matched)}')#пишем длину найденных совпадений

matched = sorted(matched,key=len)#сортируем по длине
print("Отсортированные строки:")#пишем информацию
for line in matched:#проходимся по листу
    print(line)#выводим совпадения
