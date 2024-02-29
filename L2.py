# Списки (как массивы, но любых типов данных)

# list_1 = []
# list_1 = list()
# list_1 = [1, 2, 3, 4, 5]
# #         0  1  2  3  4

# print(list_1)
# print(*list_1) # вывод без скобочек
# for i in list_1:
#     print(i)
# print(len(list_1))
# print(list_1[2])
# print(list_1[-3]) # нумерация с конца

# list_1 = [1, 5]
# print(list_1)
# list_1.append(8) # добавление элемента в конец списка
# print(list_1)

# list_1 = []
# print(list_1)
# for i in range(5):
#     list_1.append(i)
#     print(list_1)

# list_1 = [12, 7, -1, 21, 0] # Удаление последнего элемента списка
# print(list_1.pop())
# print(list_1)
# print(list_1.pop())
# print(list_1)
# print(list_1.pop())
# print(list_1)
# print(list_1.pop())
# print(list_1)
# print(list_1.pop())
# print(list_1)

# list_1 = [12, 7, -1, 21, 0] # запомнит последний элемента списка
# print(list_1)
# a = list_1.pop()
# print(list_1)
# print(a)

# list_1 = [12, 7, -1, 21, 0] # удалит i-й элемента списка
# print(list_1)
# a = list_1.pop(0)
# print(list_1)
# print(a)

# list_1 = [12, 7, -1, 21, 0] # добавит i-й элемента списка
# print(list_1.insert(3, 11))
# print(list_1)

# Срезы

# list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list_1[0])                    # 1
# print(list_1[1])                    # 2
# print(list_1[len(list_1)-1])        # 10
# print(list_1[-5])                       # 6
# print(list_1[:])                       # весь массив
# print(list_1[:2])                       # 1,2
# print(list_1[len(list_1)-2:])                       # 9,10
# print(list_1[2:9])                       # 3,4,5,6,7,8,9
# print(list_1[6:-18])                       # пустой
# print(list_1[0:len(list_1):6])                       # 1,7
# print(list_1[::6])                       # 1,7

# Кортеж (справочник)

# t = ()
# print(type(t))
# t = (1)
# print(type(t))
# t = (1, 5, 3)
# print(type(t))

# v = [1, 8, 9]
# print(v)
# print(type(v))
# v = tuple(v)
# print(v)
# print(type(v))

# a = 1
# b = 2
# a, b = 1, 2
# a = b = 1
# a, b, c = v
# print(a,b,c)
 
# t = (1, 2, 3, 5) # кортеж не поддерживает преобразование элементов

# print(t[1])
# for i in t:
#     print(i)
# for i in range(len(t)):
#     print(t[i])

# t[0] = 2 # кортеж не поддерживает преобразование элементов - эта строка выдаст ошибку

# Словари

# мы сами задаем ключ вместо индекса

# d = {}
# d = dict()
# d['q'] = 'qwerty' # q это ключ
# print(d)
# d['w'] = 'werty' # w это ключ
# print(d['w'])
# выводим все по ключу
# del d['ключ'] # удалить какой-то ключ
# for i in d:
#    print(i) # просто значения
#    print('{}: {}'.format(i, d[i])) # ключи и значения
# print(d.i())
# for (k,v) in d.i():
#   print(k,v) # k ключ v значение

# Множества

# уникальные неупорядоченные элементы

# colors = {'red', 'green', 'blue'}
# print(type(colors))
# print(colors)
# colors.add('gray')
# print(colors)
# colors.remove('red')
# print(colors)
# colors.discard('blue') # удаление с проверкой
# print(colors)
# colors.clear()
# print(colors)

# q = set()

# операции с множествами
# a = {1,2,3,5,8}
# b = {2,5,8,13,21}
# c = a.copy() # скопировать
# u = a.union(b) # объединить
# i = a.intersection(b) # пересечение
# dl = a.difference(b) # разность
# dr = b.difference(a) # разность
# q = a.union(b).difference(a.intersection(b)) # 1-int... 2-union 3-dif...

# замороженное множество

# a = {1,8,6}
# b = frozenset(a)
# print(b)

# Генератор списков

# list_1 = [exp for item in iterable] # вывести список
# list_1 = [i for i in range(1, 101)]
# list_1 = [exp for item in iterable (if conditional)] # вывести по условию 
# list_1 = [i for i in range(1, 101) if i % 2 == 0] 

# Ошибки

# Синтаксические
# Отступы
# Типов
# Деление на 0
# Ключа
# Имени переменной
# Значения
# Логику включать


# 

