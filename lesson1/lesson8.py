print('Task 1')
'''
Реализовать класс «Дата», функция-конструктор которого
должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода.
Первый, с декоратором @classmethod, должен извлекать число, месяц, год
и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod,
должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.

'''


class Data:
    def __init__(self, date):
        self.date = date

    @classmethod
    def make_num(cls, date):
        date_split = date.split('-')
        day, month, year = int(date_split[0]), int(date_split[1]), int(date_split[2])
        return day, month, year

    @staticmethod
    def validate(date):
        day, month, year = Data.make_num(date)
        if 1 <= day <= 31:
            print('Число (день) корректно')
        else:
            print('Число (день) не корректно')
        if 1 <= month <= 12:
            print('Число (месяц) корректно')
        else:
            print('Число (месяц) корректно')
        if year > 0:  # В задании не указано, что год только 4х-значный и не может быть прошлым или будущим
            print('Число (год) корректно')
        else:
            print('Число (год) не корректно')
        if month == 2 and not day <= 28:
            print('Число (день) не корректно')


print(Data.make_num('01-02-1221'))
Data.validate('11-11-42')

print('Task 2')
'''
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем.
При вводе пользователем нуля в качестве делителя программа должна
корректно обработать эту ситуацию и не завершиться с ошибкой.
'''


class ZeroDivisionReplicate(Exception):
    def __init__(self, txt):
        self.txt = txt


try:
    a = float(input('Введите число: '))
    b = float(input('Введите не нулевое число: '))
    if b == 0:
        raise ZeroDivisionReplicate('На ноль делить нельзя!')
except ZeroDivisionReplicate as err:
    print(err)
else:
    print(a/b)


print('Task 3')
'''
Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
Проверить работу исключения на реальном примере.
Необходимо запрашивать у пользователя данные и заполнять список только числами.
Класс-исключение должен контролировать типы данных элементов списка.
Примечание: длина списка не фиксирована.
Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу скрипта,
введя, например, команду “stop”.
При этом скрипт завершается, сформированный список с числами выводится на экран.
Подсказка: для данного задания примем,
что пользователь может вводить только числа и строки.
При вводе пользователем очередного элемента необходимо реализовать проверку типа элемента
и вносить его в список, только если введено число.
Класс-исключение должен не позволить пользователю ввести текст (не число)
и отобразить соответствующее сообщение. При этом работа скрипта не должна завершаться.
'''


class OnlyNums(Exception):
    def __init__(self, txt):
        self.txt = txt


list_nums = []
print('Введите stop, чтобы остановить программу')
while True:
    new_elem = input('Введите число: ')
    if new_elem == 'stop':
        break
    else:
        try:
            is_all_nums = all([ord(new_elem[i]) in [*range(48, 58), 45, 46] for i in range(len(new_elem))])
            if is_all_nums:
                list_nums.append(float(new_elem))
            else:
                raise OnlyNums('Вводите только числа или stop ')
        except OnlyNums as err:
            print(err)
            continue
print(list_nums)

print('Tasks 4, 5, 6')
'''
Поскольку эти задания - явно указанные продолжения друг друга, проще реализовать их
в рамках одного задания, чем 3 раза переписывать код
'''

'''
Начните работу над проектом «Склад оргтехники».
Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
Продолжить работу над первым заданием.
Разработать методы, отвечающие за приём оргтехники на склад и передачу
в определенное подразделение компании.
Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
можно использовать любую подходящую структуру, например словарь.
Продолжить работу над вторым заданием.
Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.

'''


class NotExist(Exception):
    def __init__(self, txt):
        self.txt = txt


class Warehouse:
    current_here = {'printer': 0, 'scanner': 0, 'xerox': 0}
    departments = {'hr': {'printer': 0, 'scanner': 0, 'xerox': 0},
                   'logistic': {'printer': 0, 'scanner': 0, 'xerox': 0},
                   'sales': {'printer': 0, 'scanner': 0, 'xerox': 0},
                   'marketing': {'printer': 0, 'scanner': 0, 'xerox': 0},
                   'IT': {'printer': 0, 'scanner': 0, 'xerox': 0},
                   'purchasing': {'printer': 0, 'scanner': 0, 'xerox': 0}}

    def add_new_type_technique(self, type_technique):
        self.current_here[type_technique] = 0

    def add_new_department(self, department):
        self.departments[department] = {k: 0 for k in self.current_here.keys()}

    def validation(self, technique='printer', department='IT', n=0):
        if technique not in self.current_here.keys():
            raise NotExist('Такая техника не зарегистрирована')
        if department not in self.departments.keys():
            raise NotExist('Такой отдел не существует')
        if type(n) != int:
            raise TypeError('Количество техники должно быть числом')

    def accept(self, new_technique: str, n: int):
        self.validation(technique=new_technique, n=n)
        self.current_here[new_technique] += n

    def move_to_department(self, technique: str, department: str, n: int):
        self.validation(technique=technique, department=department, n=n)
        if self.current_here[technique] < n:
            raise NotExist('Не достаточное количество техники на складе')
        else:
            self.current_here[technique] -= n
            self.departments[department][technique] += n


class OrgTechnique:
    def __init__(self, technique: str, n: int):
        self.technique = technique
        self.n = n

    def move_to_warehouse(self, warehouse: Warehouse):
        warehouse.accept(self.technique, self.n)
        self.n = 0


class Printer(OrgTechnique):
    def __init__(self, n):
        super().__init__('printer', n)


class Scanner(OrgTechnique):
    def __init__(self, n):
        super().__init__('scanner', n)


class Xerox(OrgTechnique):
    def __init__(self, n):
        super().__init__('xerox', n)


'''
Проверка
'''
warehouse_x = Warehouse()  # Создаем склад
new_printers = Printer(10)  # Поступила партия принтеров
new_printers.move_to_warehouse(warehouse_x)  # Отправляем на склад
new_scanners = Scanner(5)
new_scanners.move_to_warehouse(warehouse_x)
warehouse_x.move_to_department('printer', 'IT', 3)
print(warehouse_x.departments['IT'])

new_technique = OrgTechnique('PC', 50)
try:
    new_technique.move_to_warehouse(warehouse_x)
except NotExist as e:
    print(e)
    print('Регистрируем новый тип техники')
    warehouse_x.add_new_type_technique('PC')
    new_technique.move_to_warehouse(warehouse_x)


new_xeroxes = Xerox(1)
try:
    new_xeroxes.move_to_warehouse(warehouse_x)
    warehouse_x.move_to_department('xerox', 'RPA', 1)
except NotExist as e:
    print(e)
    print('Регистрируем новый отдел')
    warehouse_x.add_new_department('RPA')
    warehouse_x.move_to_department('xerox', 'RPA', 1)

warehouse_x.move_to_department('PC', 'RPA', 50)

print(warehouse_x.current_here)
print(warehouse_x.departments)

print('Tasks 7')
'''
Реализовать проект «Операции с комплексными числами». 
Создайте класс «Комплексное число», 
реализуйте перегрузку методов сложения и умножения комплексных чисел. 
Проверьте работу проекта, создав экземпляры класса (комплексные числа) 
и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.
'''


class Complex:
    def __init__(self, basis, i: int):
        self.basis = basis
        self.i = i

    def __add__(self, other):
        basis = self.basis + other.basis
        i = self.i + other.i
        return Complex(basis, i)

    def __mul__(self, other):
        x1, x2 = self.basis, other.basis
        y1, y2 = self.i, other.i
        basis = x1 * x2 - y1 * y2
        i = x1 * y2 + x2 * y1
        return Complex(basis, i)

    def __str__(self):
        return f'{self.basis}' + (f'+{self.i}i' if self.i >=0 else f'{self.i}i')


complex1 = Complex(5, -5)
print(complex1)
complex2 = Complex(5, 4)

print(complex1 + complex2)
print(complex(5, -5) + complex(5, 4))  # Проверка встроенным типом

print(complex1 * complex2)
print(complex(5, -5) * complex(5, 4))  # Проверка встроенным типом

