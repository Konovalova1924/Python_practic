# Задача1
# Требуется вычислить, сколько раз встречается некоторое число k в массиве list_1.
# Найдите количество и выведите его.
# input:
# list_1 = [1, 2, 3, 4, 5]
# k = 3
# output: 1

# list_1 = [1, 3, 3, 4, 5]
# k = 3
# count = 0
# for i in range(len(list_1)):
#     if list_1[i] == k:
#         count += 1;
# print(count) 

# Задача2:
# Требуется найти в массиве list_1 самый близкий по значению элемент 
# к заданному числу k и вывести его.
# Считать, что такой элемент может быть только один. 
# Если значение k совпадает с этим элементом - выведите его.
# input:
# list_1 = [1, 2, 3, 4, 5]
# k = 6
# output: 5

# list_1 = [1, 4, 3, 7, 8, 9, 2]
# k = 8
# i = 0
# res = 0
# for i in range(len(list_1)):
#     if (k-1) == list_1[i] or (k+1) == list_1[i]:
#         res = list_1[i]
#     elif k == list_1[i]:
#         res = list_1[i]
#         break
# print(res)

# Задача3:
# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# K – 5 очков;
# J, X – 8 очков;
# Q, Z – 10 очков.
# А русские буквы оцениваются так:
# А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного 
# пользователем слова k и выводит его. Будем считать, что на 
# вход подается только одно слово, которое содержит либо только
# английские, либо только русские буквы.
# input: k = 'ноутбук'
# output: 12
    
# alf = {'A':1, 'E':1, 'I':1, 'O':1, 'U':1, 'L':1, 'N':1, 'S':1, 'T':1, 'R':1, 'D':2, 'G':2, 'B':3, 'C':3, 'M':3, 'P':3, 'F':4, 'H':4, 'V':4, 'W':4, 'Y':4, 'K':5, 'J':8, 'X':8, 'Q':10, 'Z':10,
#         'А':1, 'В':1, 'Е':1, 'И':1, 'Н':1, 'О':1, 'Р':1, 'С':1, 'Т':1, 'Д':2, 'К':2, 'Л':2, 'М':2, 'П':2, 'У':2, 'Б':3,
#         'Г':3, 'Ё':3, 'Ь':3, 'Я':3, 'Й':4, 'Ы':4, 'Ж':5, 'З':5, 'Х':5, 'Ц':5, 'Ч':5, 'Ш':8, 'Э':8, 'Ю':8, 'Ф':10, 'Щ':10, 'Ъ':10 }

# k = 'lizard'
# k = k.upper()
# list_1 = list()

# for i in range(len(k)):
#     list_1.append(k[i])
# # print(list_1)
# # print(type(list_1))
# # print(type(alf))
# res_set = list ()

# for j in alf:
#     for i in range(len(list_1)):
#         if list_1[i] == j:
#             res_set.append(alf[list_1[i]])
#             # print(j, alf[list_1[i]])
        
# # print(res_set)
# sum = 0
# for i in range(len(res_set)):
#     sum = sum + res_set[i]
# print(sum)

# сдано


