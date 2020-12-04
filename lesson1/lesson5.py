import json  # для задания 7
print('Task1')
'''
Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
'''

with open('task1.txt', 'w') as task1:
    while True:
        new_line = input('Введите строку: ')
        if new_line == '':
            break
        else:
            task1.write(new_line + '\n')

print('Task2')
'''
Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
'''
with open('Task2.txt', 'r') as task2:
    content = task2.readlines()
k_lines = len(content)
k_words_for_strings = {i+1: len(content[i].split()) for i in range(k_lines)}
print(f'Количество строк: {k_lines}')
print(f'Количество слов по строкам: {k_words_for_strings}')

print('Task3')
'''
Создать текстовый файл (не программно), построчно записать фамилии сотрудников
и величину их окладов (не менее 10 строк).
Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.

Пример файла:
Иванов 23543.12
Петров 13749.32
'''
with open('Task3.txt', 'r') as Task3:
    content = [line.split() for line in Task3.readlines()]
    income_level = {x[0]: x[1] for x in content}
print('Доход менее 20 тыс. у следующих в списке: ', [x for x in income_level.keys()
                                                     if float(income_level[x]) < 20000])
print(f'Среднее по доходу: {sum([map(float, income_level.values())])/len(content)}')

print('Task4')
'''
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
'''
change_language = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
with open('Task4_1.txt', 'r') as Task4_1, open('Task4_2.txt', 'w') as Task4_2:
    for line in Task4_1:
        key = line.split(' — ')[0]
        Task4_2.write(line.replace(key, change_language[key]))

print('Task5')
'''
Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
'''
'''
Комментарий к заданию. Не вполне ясная формулировка. Сначала записать в файл, а затем прочитать
из файла и посчитать?
Выполнено исходя из этого предположения.
'''
with open('Task5.txt', 'w+') as Task5:
    print(input('Введите числа через пробел: '), file=Task5)
    Task5.seek(0)
    content = Task5.read()
    sum_nums = sum(map(float, content.split()))
print(sum_nums)
print('Task6')
'''
Необходимо создать (не программно) текстовый файл,
где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
Вывести словарь на экран.
Примеры строк файла:

Информатика:   100(л)   50(пр)   20(лаб).
Физика:        30(л)     —       10(лаб)
Физкультура:   —        30(пр)     —

Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

'''
subjects = {}


def is_numeric_n(x):
    return True if 48 <= ord(x) <= 57 else False


with open('Task6.txt', 'r') as Task6:
    for line in Task6:
        split_file = line.split(':')
        name, k_subj = split_file[0], ''.join([x for x in split_file[1] if 48 <= ord(x) <= 57 or ord(x) == 40])
        print(k_subj.split('('))
        take_nums = [int(x) for x in k_subj.split('(')]
        subjects[name] = sum(take_nums)


print(subjects)
print('Task7')
'''
Создать вручную и заполнить несколькими строками текстовый файл, 
в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки. 
Пример строки файла: 
firm_1   ООО   10000   5000.
Необходимо построчно прочитать файл, 
вычислить прибыль каждой компании, 
а также среднюю прибыль. 
Если фирма получила убытки, в расчет средней прибыли ее не включать.

Далее реализовать список. 
Он должен содержать словарь с фирмами и их прибылями, 
а также словарь со средней прибылью. 
Если фирма получила убытки, также добавить ее в словарь (со значением убытков). 
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджер контекста.

'''
profit = {}  # Словарь с прибылями и убытками фирм
with open('Task7.txt', 'r') as Task7:
    for line in Task7:
        split_line = line.split()
        profit[split_line[0]] = float(split_line[-2]) - float(split_line[-1])

profited_firms = [x for x in profit.values() if x >= 0]  # по условию мы не включаем только убыточные фирмы
average_profit = sum(profited_firms) / len(profited_firms)

with open('Task7_2.json', 'w') as Task7_2:
    json.dump([profit, {"average_profit": average_profit}], Task7_2)