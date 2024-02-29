# Функция
# обозначается как def имя (параметры)

# def sum_numbers(n):
#     summa = 0
#     for i in range(1, n+1):
#         summa +=i
#     print(summa)
# sum_numbers(5)

# def sum_numbers(n):
#     summa = 0
#     for i in range(1, n+1):
#         summa +=i
#     return summa
# print(sum_numbers(5))

# def sum_numbers(n):
#     summa = 0
#     for i in range(1, n+1):
#         summa +=i
#     return summa
# a = sum_numbers(5)
# print(a)

# def sum_numbers(n, y = 'Hello'):
#     summa = 0
#     for i in range(1, n+1):
#         summa +=i
#     return summa
# a = sum_numbers(5, 'qwert')
# print(a)

# функция с неограниченным количеством аргументом

# def sum_str(*args):
#     res = ''
#     for i in args:
#         res += i
#     return res
# print(sum_str('q', 'e', 'l'))
# print(sum_str('q', 'e', 'l', 'r'))
# print(sum_str(1, 8, 9))

# Модульность

# Модуль это отдельный файл modul.py, 
# в котором описано много функций, которые можно использовать

# импортируем этот файл сюда

# вариант1
# import L3modul
# print(L3modul.max1(5, 9))

# вариант2
# from L3modul import max1
# print(max1(10, 9))

# вариант3 все функции импортировать
# from L3modul import *
# print(max1(10, 9))

# импортировать с другим коротким именем 
# import L3modul as L31
# print(L31.max1(10, 9))

# Рекурсия - функция, которая вызывает сама себя

# def fib(n):
#     if n in [1,2]:
#         return 1
#     return fib(n-1) + fib(n-2)

# list_1 = []
# for i in range(1, 10):
#     list_1.append(fib(i))
# print(list_1)

# Алгоритмы сортировки с рекурсией

# быстрая сортировка

# def quick_sort(array):
#     if len(array) <= 1:
#         return array
#     else:
#         pivor = array[0]
#     less = [i for i in array[1:] if i <= pivor]
#     greater = [i for i in array[1:] if i > pivor]
#     return quick_sort(less) + [pivor] + quick_sort(greater)
# print(quick_sort([14, 5, 9 ,6, 3, 58, 7, 5, 2, 7]))

# сортировка слиянием

# def merge_sort(nums):
#     if len(nums) > 1:
#         mid = len(nums) // 2
#         left = nums[:mid]
#         right = nums[mid:]
#         merge_sort(left)
#         merge_sort(right)
#         i = j = k = 0
#         while i < len(left) and j < len(right):
#             if left[i] < right[j]:
#                 nums[k] = left[i]
#                 i +=1
#             else:
#                 nums[k] = right[j]
#                 j +=1
#             k +=1
#         while i < len(left):
#             nums[k] = left[i]
#             i +=1
#             k +=1
#         while j < len(right):
#             nums[k] = right[j]
#             j +=1
#             k +=1
        
# list_1 = [1,5,6,9,8,7,2,1,55,2,4]
# merge_sort(list_1)
# print(list_1)

###
