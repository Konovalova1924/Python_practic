# a = 1
# b = 'kiss'
# c = 2.56
# print(f"{a}-{b}-{c}")
# print("{}-{}-{}".format(a,b,c))

# print('Введите первое число:')
# a = input()
# b = input('Введите второе число:')
# print(a, " + ", b, " = ", a + b)

# c = 5.89
# print(c)
# print(type(c))
# c = str(c)
# print(c + ' 67')
# print(type(c))

# c = 1
# print(c)
# print(type(c))
# c = bool(c)
# print(c)
# print(type(c))

# print('Введите первое число:')
# a = int(input())
# b = int(input('Введите второе число:'))
# print(a, " + ", b, " = ", a + b)

# a = 5.786987
# b = 6.87878
# print(round(a*b, 3)) 

# iter = 2
# iter +=3 # к iter прибавить 3
# iter -=4 # от iter отнять 4
# iter *=5 # iter * 5
# iter /=5 # iter / 5
# iter //=5 # iter // 5
# iter %=5 # iter % 5
# iter **=5 # iter ** 5

# a = 1 > 4
# print(a)
# a = 1 > 4 and 5 > 2
# print(a)
# a = 1 == 2
# print(a)
# a = 1 != 2
# print(a)
# a = 'qqe'
# b = 'qqe'
# print(a == b)
# a = 1 < 3 < 3 < 10
# print(a)

#!!!  if else !!!#

# username = input('Введите имя:')
# if username == 'Маша':
#     print('Ура, это же Маша!')
# elif username == 'Марина':
#     print('Я так ждала вас, Марина!')
# elif username == 'Ильнар':
#     print('Ильнар - топ')
# else:
#     print('Привет, ', username)
    
# while #

# n = 5678
# summa = 0
# while n > 0:
#     x = n % 10
#     summa = summa + x
#     n = n // 10
# print(summa)

# while else #

# i = 0
# while i < 5:
#     if i == 3:
#         break             #лучше обойтись без него в чистом коде
#     i = i + 1
# else:                     #будет работать если закоментить строки 84, 85
#     print('пожалуй')
#     print('хватит )')
# print(i)

#флажок вместо break#

# n = int(input())
# flag = True
# i = 2
# while flag == True:
#     if n % i == 0:
#         flag = False
#         print(i)
#     elif i > n // 2:
#         print(n)
#         flag = False
#     i = i + 1

# for #
# range (начало, конец, шаг) # конец-1

# r = range(5)
# r = range(2,5)
# r = range(100,0,-20)
# for i in r:
#     print(i)

# a = 'qwerty'
# print(a[0])
# for i in a:
#     print(i)

# line = ""
# for i in range(5):
#     line = ""
#     for j in range(5):
#         line = line + "*"
#     print(line)

# строки #

# text = "вив втт кепкеп ыукпк иа ыкпи"
# print(len(text))
# print("втт" in text)
# print(text.lower())
# print(text.upper())
# print(text.replace('втт', 'ВТТ'))

# срезы #

# print(text[0])
# print(text[len(text)-1])
# print(text[-1])
# print(text[-4])
# print(text[:])
# print(text[:2])
# print(text[20:])
# print(text[2:9])
# print(text[0:len(text):6]) # как range(a,b,c)

# text = text[0] + text[len(text)-1] + text[-1] + text[-4] + text[:] + text[:2] + text[20:] + text[2:9] + text[0:len(text):6]
# print(text)
