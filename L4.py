# Функции высшего порядка, работа с файлами

# def f(x):
#     return x*x

# print(f(5))
# print(type(f))
# a = f
# print(type(a))
# print(a(5))

# def calk1(a,b):
#     return a+b

# def calk2(a,b):
#     return a*b

# def math(op, x, y):
#     print(op(x, y))

# math(calk1, 5, 45)
# math(calk2, 5, 45)

# ЛЯмбда Функции

# calk1 = lambda a,b: a + b

# calk2 = lambda a,b: a*b

# math(lambda a,b: a + b, 5, 45)

# задача:
# в списке хранятся числа. нужно выбрать только четные 
# и составить список пар (число: квадрат числа)
# 1 2 3 5 8 15 23 38
# [(2,4), (8,64), (38, 1444)]

# list1 = [1, 2, 3, 5, 8, 15, 23, 38]
# res = list()
# for i in range(1,len(list1)):
#     if i%2 == 0:
#         res.append((i, i**2))      
# print(res)

# def select(f,col):
#     return [f(x) for x in col]

# def where(f, col):
#     return [x for x in col if f(x)]

# data = [1, 2, 3, 5, 8, 15, 23, 38]
# res = select(int, data)
# print(res)
# res = where(lambda x: x % 2 == 0, res)
# print(res)
# res = list(select(lambda x: (x, x**2), res))
# print(res)

# Функция map

# list_1 = [x for x in range(1, 20)]
# print(list_1)
# list_1 = list(map(lambda x: x + 10, list_1))
# print(list_1)

# Задача

# data = ' 15 156 96 3 5 8 52 5'
# print(data)
# вариант 1
# data = data.split()
# print(data)
# вариант 2
# data = list(map(int, data.split()))
# print(data)

# select можно заменить на map. select прописывается явно, map прописано где-то.

# функция filter

# data = [15,65,9,36,175]
# res = list(filter(lambda x: x % 10 == 5, data))
# print(res)

# where можно заменить на filter.

# функция zip

# функция enumerate

# Файлы

# завести переменную, которая будет связана с этим текстовым файлом
# указать путь к файлу
# указать в каком режиме мы будем работать с файлом
# режимы
# а - открыть для добавления данных
# r - открыть для чтения данных
# w - открыть для записи данных
# w+ - открыть и читать
# r+ - отрыть и дописывать

# colors = ['red' ,'green', 'blue', '945985']
# data = open('file.txt', 'a')
# data.writelines(colors)
# data.close()

# with open('file.txt', 'w') as data:
#     data.write('line 1\n')
#     data.write('line 32\n')

# path = 'file.txt'
# data = open('file.txt', 'r')
# for line in data:
#     print(line)
# data.close()

# Модуль OS

# Модуль shutil

###


