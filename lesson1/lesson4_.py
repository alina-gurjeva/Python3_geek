from functools import reduce, lru_cache
from itertools import count, cycle
from sys import argv

print('Задание 1')
'''1)Реализовать скрипт,в котором должна быть предусмотрена
функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.'''
hours, salary_per_hour, bonus = argv[1], argv[2], argv[3]  # argv[0] - это название модуля


def count_salary(hours_, salary_per_hour_, bonus_):
    return int(hours_) * float(salary_per_hour_) + float(bonus_)


print(count_salary(hours, salary_per_hour, bonus))

print('Задание 2')
'''
Представлен список чисел.
Необходимо вывести элементы исходного списка,значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
Для формирования списка использовать генератор. Пример исходного списка:
[300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].
'''
example_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print([example_list[i] for i in range(1, len(example_list)) if example_list[i] > example_list[i-1]])

print('Задание 3')
'''
Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21.
Необходимо решить задание в одну строку.
Подсказка: использовать функцию range() и генератор.
'''
'''
УСЛОВИЕ не корректно: неясно, включая границы либо нет. => 2 варианта:
'''
# 1 вариант
print([x for x in range(20, 241) if x % 20 == 0 or x % 21 == 0])  # Если имелось в виду, включая границы
# 2 вариант
print([x for x in range(21, 240) if x % 20 == 0 or x % 21 == 0])  # Если имелось в виду, НЕ включая границы

print('Задание 4')
'''
Представлен список чисел.
Определить элементы списка, не имеющие повторений.
Сформировать итоговый массив чисел, соответствующих требованию.
Элементы вывести в порядке их следования в исходном списке.
Для выполнения задания обязательно использовать генератор.
Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
Результат: [23, 1, 3, 10, 4, 11]
'''
numbers = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result_list = [x for x in numbers if numbers.count(x) == 1]
print(result_list)

print('Задание 5')
'''
Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce()
'''
even_nums = [x for x in range(100, 1001) if x % 2 == 0]


def multi(a, b):
    return a * b


print(reduce(multi, even_nums))

print('Задание 6')
'''
Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools.
Обратите внимание, что создаваемый цикл не должен быть бесконечным.
Необходимо предусмотреть условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3,
а при достижении числа 10 завершаем цикл.
Во втором также необходимо предусмотреть условие, при котором
повторение элементов списка будет прекращено.
'''
# a)
# 1 вариант решения
start = 5
stop = 15
for x in count(start):
    if x < stop:
        print(x)
    else:
        break
# 2 вариант решения
n_elements = 10
iter_start = count(start)
for i in range(n_elements):
    print(next(iter_start))
# b)
repeat_list = ['*', '***', '*****']
repeat_iter = cycle(repeat_list)
n_repeat = len(repeat_list) * 3
for i in range(n_repeat):
    print(next(repeat_iter))

print('Задание 7')
'''
Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
При вызове функции должен создаваться объект-генератор.
Функция должна вызываться следующим образом: for el in fact(n).
Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые n чисел, 
начиная с 1! и до n!.
Подсказка: факториал числа n—произведение чисел от 1 до n.
Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24
'''

'''
"выводить только первые n чисел, начиная с 1! и до n!" звучит  непонятно, 
как понять "ПЕРВЫЕ n чисел". Решение, если имелось в виду,
что для указанного n функция должна генерировать числа: 1! 2! ... n!
 '''


# Функция факториала есть в модуле math, однако не известно разрешено ли ее использовать.
# 1й вариант функции факториала.
@lru_cache(maxsize=None)
def factorial(x):
    if x == 0 or x == 1:
        return 1
    else:
        return x * factorial(x-1)


# 2й вариант функции факториала.
def factorial_(x):
    if x == 0 or x == 1:
        return 1
    answer = 1
    for i in range(1, x+1):
        answer *= i
    return answer


# Собственно, задание:
def fact(y):
    for i in range(1, y+1):
        yield factorial(i)


n = 10
for el in fact(n):
    print(el)
