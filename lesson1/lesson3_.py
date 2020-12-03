print('Задание 1')
'''
Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
'''


def division(a, b):
    try:
        return int(a) / int(b)
    except ZeroDivisionError:
        print('На ноль делить нельзя!')
    except ValueError:
        print('Неподходящие типы данных')


'''Второй вариант (тк оказалось, что try except нельзя)'''


def division1(a, b):
    if b == 0:
        return 'На ноль делить нельзя!'
    else:
        return int(a) / int(b)


print(division(input('Введите делимое: '), input('Введите делитель: ')))

print('Задание 2')
'''
Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
'''


def info2(**kwargs):
    arguments = kwargs
    true_names = {'name', 'surname', 'year_birthday', 'city', 'email', 'phone'}
    if len(set(arguments.keys()) | true_names) != len(true_names):  # Проверка на лишние аргументы
        raise Exception("Можно передать только: 'name', 'surname', 'year_birthday', 'city', 'email', 'phone'")
    data = [[x[0], str(x[1])] for x in arguments.items()]
    return ', '.join(list(map(lambda x: ': '.join(x), data)))


'''Внимание. Предупреждая вопросы, что нельзя "raise Exception" - в этом задании 
можно заменить строку тоже на return, как пример: '''


def info2_basic(**kwargs):
    arguments = kwargs
    true_names = {'name', 'surname', 'year_birthday', 'city', 'email', 'phone'}
    if len(set(arguments.keys()) | true_names) != len(true_names):  # Проверка на лишние аргументы
        return "Ошибка. Можно передать только: 'name', 'surname', 'year_birthday', 'city', 'email', 'phone'"
    data = [[x[0], str(x[1])] for x in arguments.items()]
    return ', '.join(list(map(lambda x: ': '.join(x), data)))


# В задании не указано, что данные д. вводить пользователь
# Примеры
print(info2(name='Beard', year_birthday=1801, city='Transilvania'))
print(info2(year_birthday=1703, city='Necropolis', name='Abraham'))
print(info2_basic(year_birthday=1703, city='Necropolis', name='Abraham'))

print('Задание 3')
'''
Реализовать функцию my_func(),
которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
'''


def my_func(a, b, c):
    arguments = [a, b, c]
    arguments.remove(min(arguments))
    return arguments[0] + arguments[1]


# В задании не указано, что данные д. вводить пользователь
# Примеры
print(my_func(1, 2, -3))
print(my_func('*', '4', '2'))
print(my_func([], [1], [1, 2]))

print('Задание 4')
'''
Программа принимает действительное положительное число x и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y.
Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **. 
Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
'''


# 1й способ
def my_func1(x: float, y: int):
    if not all([x > 0, y < 0]):
        raise Exception('Второй аргумент должен быть отрицательным')
    return 1 / (x ** abs(y))


# 2й способ - можно использовать цикл, можно решить рекурсией
def my_func2(x: float, y: int):
    if not all([x > 0, y < 0]):
        raise Exception('Второй аргумент должен быть отрицательным')

    def inner_pow(a, b):
        if b == 1:
            return a
        return a * inner_pow(a, b - 1)

    return 1 / inner_pow(x, abs(y))


try:
    print(my_func1(float(input('Введите действительное положительное число: ')),  # Тест 1й функции
                   int(input('Введите целое отрицательное число: '))))
    print(my_func2(float(input('Введите действительное положительное число: ')),  # Тест 2й функции
                   int(input('Введите целое отрицательное число: '))))
except ValueError:
    print('Неверный тип данных')

'''И опять поправка насчет "нельзя Exception, тогда функции можно и так (заодно решу через циклы) '''


def my_func1(x: float, y: int):
    if not all([x > 0, y < 0]):
        print('Ошибка. Второй аргумент должен быть отрицательным')
        return 0
    a = 1
    for i in range(y):
        a *= x
    return 1 / a


'''Тогда изменится и вызов функций (при неверном типе данных будет падать стандартная ошибка ValueError: '''
print(my_func1(float(input('Введите действительное положительное число: ')),  # Тест 1й функции
               int(input('Введите целое отрицательное число: '))))

print('Задание 5')
'''
Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел.
Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введен после нескольких чисел,
то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.

'''


def is_digit_num(x: str):
    if all(48 <= ord(i) <= 57 for i in x):
        return True
    else:
        return False


sum_all_nums = 0
flag = 0  # Нужен, чтобы не выводить sum_all_nums раньше первого input

print('Программа завершится при попытке ввести строчный символ')
while True:
    if flag:
        print(sum_all_nums)
    part_nums = [x for x in input('Введите числа, разделенные пробелом: ').split(' ')]
    flag = 1
    types = [is_digit_num(x) for x in part_nums]
    if False in types:
        ind = types.index(False)
        remainder = part_nums[:ind]
        sum_all_nums += sum([float(x) for x in remainder])
        break
    else:
        sum_all_nums += sum([float(x) for x in part_nums])


print('Задание 6')
'''
Реализовать функцию int_func(), принимающую слово из маленьких латинских букв
и возвращающую его же, но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.

Продолжить работу над заданием.
В программу должна попадать строка из слов, разделенных пробелом.
Каждое слово состоит из латинских букв в нижнем регистре.
Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
Необходимо использовать написанную ранее функцию int_func().
'''
# 1й вариант решения (более простой)
import re  # Нужно проверить является ли слово словом из маленьких латинских букв


def int_func(word: str):
    if re.search(r'[^a-z]', word) is None:
        return word.title()
    else:
        raise Exception('Слово должно состоять из маленьких латинских букв')


print(' '.join([int_func(w) for w in input('Введите строку из слов, разделенных пробелом: '
                                           'Слова должны состоять из '
                                           'латинских букв в нижнем регистре: ').split(' ')]))

# 2й вариант решения. (без использования доп. библиотек)


def int_func_(word: str):
    true_symbols = [97 <= ord(x) <= 122 for x in word]
    if not all(true_symbols):
        print('Ошибка. Слово должно состоять из маленьких латинских букв')
        return 0
    return chr(ord(word[0])-32) + word[1:]


print(' '.join([int_func_(w) for w in input('Введите строку из слов, разделенных пробелом: '
                                            'Слова должны состоять из '
                                            'латинских букв в нижнем регистре: ').split(' ')]))

