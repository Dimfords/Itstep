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
#     print( "\"Don't let the noise of others' opinions \n drown out your own inner voice.\"\n \t \t \tSteve Jobs \"")

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
Напишите функцию, которая отображает горизонтальную или вертикальную линию из некоторого символа.
Функция принимает в качестве параметра: длину линии,
направление, символ. """

# def graph(length, direction, symbol):
#     for i in range(length):
#         if direction == "x":
#             print(symbol, end="")
#         else:
#             print(symbol)
            
# graph(10,"y","*")

""" Задание 4
Напишите функцию, которая возвращает максимальное из четырёх чисел. Числа передаются в качестве
параметров.
 """

# def max_fun(a,b,c,d):
#     return max(a,b,c,d)

# print(max_fun(1,2,3,4))


""" Задание 5
Напишите функцию, которая возвращает сумму чисел
в указанном диапазоне. Границы диапазона передаются
в качестве параметров. """

def sum_fun(start, end):
    if end > start:
        l = [x for x in range(start,end)]
        print(sum(l))
    else: 
        l = [x for x in range(end,start)]
        print(sum(l))

    

sum_fun(1,10)
sum_fun(10,1)