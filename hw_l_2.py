"""1. Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных
каждого элемента. Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у пользователя,
а указать явно, в программе.
"""

my_list = [1, 1.5, True, False, None, 'Text', ['ли', 'ст'], ('кор', 'теж'), {'словарь': 'dict', 'dict': 'словарь'},
           {'мно', 'жес', 'тва'}]

for i in my_list:
    print(f'{i} is {type(i)}')

"""
2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами 0 и 1, 
2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте. Для заполнения списка элементов 
 необходимо использовать функцию input().
"""

x_list = list(input("Введите числа: "))

for x in range(1, len(x_list), 2):
    x_list[x - 1], x_list[x] = [x_list[x], x_list[x - 1]]

print(x_list)

"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц 
(зима, весна, лето, осень). Напишите решения через list и через dict.
"""

d_month = {1: "Январь", 2: "Февраль", 3: "Март", 4: "Апрель", 5: "Май", 6: "Июнь",
           7: "Июль", 8: "Август", 9: "Сентябрь", 10: "Октябрь", 11: "Ноябрь", 12: "Декабрь"}
d = d_month

while True:
    month = int(input("Введите порядковый номер месяца: "))
    m = month
    if m in d:
        print(f"{m} - {d[m]}")
        break
    else:
        print("Нужно ввести число от 1 до 12")

"""
4. Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки. 
Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.
"""

x = input("Введите фразу или набор слов: ").split()

for a, b in enumerate(x, 1):
    print(a, b) if len(b) <= 10 else print(a, b[:10])

"""
5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел. 
У пользователя необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми 
значениями, то новый элемент с тем же значением должен разместиться после них.
"""

x_list = [9, 8, 7, 6, 5, 4, 3, 2, 1]
a = int(input("Введите число: "))
y = 0
for b in x_list:
    if a <= b:
        y += 1
    else:
        break
x_list.insert(y, a)
print(x_list)

"""
Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. Каждый кортеж хранит 
информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь с параметрами 
(характеристиками товара: название, цена, количество, единица измерения). Структуру нужно сформировать программно, 
т.е. запрашивать все данные у пользователя.
"""

inventory_tuple_list = []
i = 1
while True:
    inventory_tuple_list.append(
        (input('Введите номер товара: '), dict({
            'название': str(input('Введите название: ')),
            'цена': float(input('Введите цену: ')),
            'количество': int(input('Введите количество: ')),
            'eд': str(input('Введите единцы измерения: ')),
        }))
    )

    if input('Товар добавлен. Добавить еще один товар? (да/нет): ') == 'нет':
        break

    i += 1

print(f'список товаров:{inventory_tuple_list}')

output_dict = dict({})
for product in inventory_tuple_list:
    for key, value in product[-1].items():
        if key in output_dict:
            if value not in output_dict.get(key):
                output_dict.get(key).append(value)
        else:
            output_dict.update({key: [value]})

print(f'собрана аналитика: {output_dict}')
