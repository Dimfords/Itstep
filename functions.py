# def print_hello(qty):
#     for x in range(qty):
#         print('Hello')

# print_hello(10)


""" Задание 1
Напишите функцию, которая отображает на экран
форматированный текст, указанный ниже:
“Don't let the noise of others' opinions
drown out your own inner voice.”
Steve Jobs """


# def str_print():
#     print( "\"Don't compare yourself with anyone in this world…\nif you do so, you are insulting yourself.\"\n \t \t \t\t \tBill Gates")

# str_print()

""" Задание 2
Напишите функцию, которая принимает два числа
в качестве параметра и отображает все нечетные числа
между ними. """

# def nechet_4isla(a, b):
#     chisla = []
#     if a < b:
#          for x in range(a, b):
#             chisla.append(x)
#     for x in range(b, a):
#             chisla.append(x)
#     for i in chisla:
#         if i % 2 == 0:
#             print(i, end=" ")

# nechet_4isla(10,1)

""" Задание 3
Напишите функцию, которая отображает пустой или
заполненный квадрат из некоторого символа. Функция
принимает в качестве параметров: длину стороны квадрата, символ и переменную логического типа:
■ если она равна True, квадрат заполненный;
■ если False, квадрат пустой. """

# def graph(length, symbol, full_empty):
#     if full_empty is True:
#         for i in range(length):
#             print("\n", end="")
#             for j in range(length):
#                 print(symbol,end=" ")
#     elif full_empty is False:
        
#         for i in range(length):
#             print(symbol,end=" ")
        
#         for i in range(length-2):
#             print("\n", end="")
#             for j in range(length):
#                 if j == 0 or j == 3:
#                     print(symbol,end=" ")
#                 print(" ", end=" ")
#         print("\n", end="")
#         for i in range(length):
#             print(symbol,end=" ")
            
# graph(5,".",False)

""" Задание 4
Напишите функцию, которая возвращает минимальное
из пяти чисел. Числа передаются в качестве
параметров.
 """

# def min_fun(a,b,c,d,e):
#     return min(a,b,c,d,e)

# print(min_fun(1,1,3,4,4))


""" Задание 5
Напишите функцию, которая возвращает сумму чисел
в указанном диапазоне. Границы диапазона передаются
в качестве параметров. Если границы диапазона перепутаны (например, 5 — верхняя граница, 25 —
нижняя граница), их нужно поменять местами.
 """

# def sum_fun(start, end):
#     if end > start:
#         l = [x for x in range(start,end)]
#         print(sum(l))
#     else: 
#         l = [x for x in range(end,start)]
#         print(sum(l))

    

# sum_fun(1,10)
# sum_fun(10,1)

""" Задание 6
Напишите функцию, которая считает количество
цифр в числе. Число передаётся в качестве параметра. Из
функции нужно вернуть полученное количество цифр.
Например, если передали 3456, количество цифр будет 4. """

# def len_gidgit(chislo):
#     return len(str(chislo))

# print(len_gidgit(6656559))

""" Задание 7
Напишите функцию, которая проверяет является ли
число палиндромом. Число передаётся в качестве параметра. Если число палиндром нужно вернуть из функции
true, иначе false.
«Палиндром» — это число, у которого первая часть
цифр равна второй перевернутой части цифр. Например,
123321 — палиндром (первая часть 123, вторая 321, которая
после переворота становится 123), 546645 — палиндром,
а 421987 — не палиндром.  """

