# comment
"""
comment
comment
"""
# ctrl + /

# 1. За день машина проезжает n километров. Сколько дней нужно, чтобы проехать маршрут длиной m километров? 
# При решении этой задачи нельзя пользоваться условной инструкцией if и циклами.
# **Input:**
# n = 700
# m = 750
# **Output:**
# 2
# **Input:**
# n = 500
# m = 500
# **Output:**
# 1

# n = int(input("Введите число: "))
# m = int(input("Введите число: "))

# print((m + n - 1) // n)

# # 13 / 5 = 2.6
# # 13 // 5 -> 2(3 ост) = 2
# # 13 % 5 -> 2(3 ост) = 3

# -------------------------------------------------------------------------------------------------------------

# 3. В некоторой школе решили набрать три новых математических класса и оборудовать кабинеты для них новыми партами. 
# За каждой партой может сидеть два учащихся. Известно количество учащихся в каждом из трех классов. 
# Выведите наименьшее число парт, которое нужно приобрести для них.
# **Input:**
# 20
# 21
# 22
# **Output:**
# 32 (10 + 11 + 11)

# 20          21
# 20          21
# 20          21
# -> 30       -> 33

# n = int(input("Введите число: "))
# m = int(input("Введите число: "))
# k = int(input("Введите число: "))
# print((n + 1) // 2 + (m + 1) // 2 + (k + 1) // 2)

# --------------------------------------------------------------------------------------------------------------------------

# n = int(input("Введите число: "))
# if n > 5:
#     print("число больше 5")
# elif n == 5:
#     print("число равно 5")
# else:
#     print("число меньше 5")

# --------------------------------------------------------------------------------------------------------------------------
# 5. Вагоны в электричке пронумерованы натуральными числами, начиная с 1 (при этом иногда
# вагоны нумеруются от «головы» поезда, а иногда – с «хвоста»; это зависит от того, в какую сторону едет электричка).
# В каждом вагоне написан его номер. Витя сел в i-й вагон от головы поезда и обнаружил, что его вагон имеет номер j.
# Он хочет определить, сколько всего вагонов в электричке. Напишите программу, которая будет это делать или сообщать, 
# что без дополнительной информации это сделать невозможно.

# **Input:**
# 3
# 4
# **Output:**
# 6
#        
#        i
#  1  2  3  4  5  6 
# -- -- -- -- -- --  
#  6  5  4  3  2  1
#        j

#        j
#        i
#  1  2  3  4  5  
# -- -- -- -- --  
#  5  4  3  2  1
#        

# i = int(input("Введите число: "))
# j = int(input("Введите число: "))

# if i == j:
#     print("без дополнительной информации решить задачу невозможно")
# else:
#     print(i + j - 1)

# --------------------------------------------------------------------------------------------------

# n = 5
# m = 1
# if n == 5 or m == 10:
#     print('ok')


# --------------------------------------------------------------------------------------------------
# 7. Дано натуральное число. Требуется определить, является ли год с данным номером високосным. Если год является високосным,
# то выведите YES, иначе выведите NO. Напомним, что в соответствии с григорианским календарем, год является високосным, 
# если его номер кратен 4, но не кратен 100, а также если он кратен 400.
# **Input:**
# 2016
# **Output:**
# YES
# 2012 -> YES
# 2018 -> NO

# year = int(input("Введите число: "))

# if year % 400 == 0 or year % 4 == 0 and year % 100 != 0 :
#     print('yes')
# else:
#     print('no')
    
    