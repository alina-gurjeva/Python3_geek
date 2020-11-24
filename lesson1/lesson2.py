from pprint import pprint
print('Задание 1')
'''
1. Создать список и заполнить его элементами различных типов данных.
Реализовать скрипт проверки типа данных каждого элемента.
Использовать функцию type() для проверки типа.
Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
'''
list_of_different_objects = [1, 2.3, 'Rock', {1, 2, 3}, {'Name': 'Harry', 'Surname': 'Potter'}, [1, 3, 4],
                             b'code', None, print, (1, 2, 3)]  # etc.
list_of_different_types = [type(x) for x in list_of_different_objects]
print(*list_of_different_types, sep='\n')

print('Задание 2')
'''
2. Для списка реализовать обмен значений соседних элементов,
т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
'''
# Ввод данных
k_elem = int(input('Введите количество элементов: '))
elements = [input(f'Введите {i+1} элемент из {k_elem}: ') for i in range(k_elem)]
# Обработка
even, uneven = elements[1::2], elements[::2]
last_element = False if len(even) == len(uneven) else uneven.pop()
reversed_elements = sum([list(x) for x in zip(even,uneven)], [])
if last_element:
    reversed_elements.append(last_element)
# Вывод
print(*reversed_elements, sep='\n')

print('Задание 3')
'''
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
'''


def season(numeric_month):
    months = [12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    seasoned_months = [months[i : i + 3] for i in range(0, 12, 3)]
    seasons = {'зима': seasoned_months[0], 'весна': seasoned_months[1], 'лето': seasoned_months[2],
               'осень': seasoned_months[3]}

    return [k for k in seasons.keys() if numeric_month in seasons[k]][0]


print(season(int(input('Введите число от 1 до 12 - номер месяца: '))))

print('Задание 4')
'''
4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
Вывести каждое слово с новой строки.
Строки необходимо пронумеровать.
Если слово длинное, выводить только первые 10 букв в слове.
'''
words = [x for x in input('Введите строку из нескольких слов, разделённых пробелами: ').split(' ')]
for i, w in enumerate(words):
    print(i, w if len(w) <= 10 else w[:10])

print('Задание 5')
'''
5. Реализовать структуру «Рейтинг», представляющую собой
не возрастающий набор натуральных чисел.
У пользователя необходимо запрашивать новый элемент рейтинга.
Если в рейтинге существуют элементы с одинаковыми значениями,
то новый элемент с тем же значением должен разместиться после них.
Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
Набор натуральных чисел можно задать непосредственно в коде,
 например, my_list = [7, 5, 3, 3, 2].
'''


class Rating:
    def __init__(self, first_list=[]):
        self.length = len(first_list)
        self.rating_dict = {} if not first_list else {k: v for k, v in enumerate(first_list)}

    def input_number(self, y: int):
        self.rating_dict[self.length] = y
        self.length += 1
        ordered_elements = sorted(self.rating_dict.items(), key=lambda x: (x[1], x[0]), reverse=True)
        return [x[1] for x in ordered_elements]


rating = Rating([1, 2, 3, 4, 1, 2])  # Можно начать и с пустого списка: rating = Rating()
print('Для остановки программы введите 0')  # Т.к. 0 не явл. натуральным числом
while True:
    number = input('Введите число: ')
    if number == '0':
        break
    else:
        try:
            number = int(number)
            if number < 0:
                print('Отрицательное число не подходит. Введите натуральное число. ')
                continue
            print(rating.input_number(number))
        except ValueError:
            print('Строка не подходящее значение. Введите число. ')
            continue

print('Задание 6')
'''
6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь с параметрами (характеристиками товара: название, цена, количество, единица измерения). Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
Пример готовой структуры:
[

(1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
(2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}), 
(3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})

]
Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара, например название, а значение — список значений-характеристик, например список названий товаров.
Пример:
{

“название”: [“компьютер”, “принтер”, “сканер”],
“цена”: [20000, 6000, 2000],
“количество”: [5, 2, 7],
“ед”: [“шт.”]

}
'''


class Goods:
    def __init__(self):
        self.index_g = 1
        self.goods = []
        self.sample_dict = {'название': '', 'цена': 0, 'количество': 0, 'eд': 'шт.'}

    def add_element(self):
        current_dict = self.sample_dict.copy()
        current_dict['название'] = input('Введите название: ')
        current_dict['цена'] = input('Введите цену: ')
        current_dict['количество'] = input('Введите количество: ')
        current_dict['eд'] = input('Введите eд. измерения: ')

        try:
            current_dict['цена'] = int(current_dict['цена'])
            current_dict['количество'] = int(current_dict['количество'])
        except ValueError:
            raise Exception('Цена и количество должны быть числами. ')

        if current_dict['цена'] < 0 or current_dict['количество'] < 0:
            raise Exception('Цена и количество могут принимать только положительные значения')

        new_good = (self.index_g, current_dict)
        self.index_g += 1
        self.goods.append(new_good)
        return self.goods


your_goods = Goods()
nums = int(input('Введите количество элементов: '))
i = 0
changed_goods = 'Элементов нет '
while i < nums:
    try:
        changed_goods = your_goods.add_element()
        i += 1
    except Exception as e:
        print(e)
        continue
pprint(changed_goods)