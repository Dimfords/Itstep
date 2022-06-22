""" 1.Написать программу, которая осуществляет перестановку элементов списка
(заполненный случайными числами в диапазоне от -5 до 5) без использования
дополнительного списка. Например:
исходный список 2 4 -2 0 -3 -1 0 1 1 3
 измененный список 3 1 1 0 -1 -3 0 -2 4 2 """

# import random

# src_list = []

# print("исходный список   --> ", end="")
# for i in range(0,10):
#     src_list.append(random.randint(-5,5))
#     print(src_list[i], end=" ")

# src_list.reverse()

# print("\nизмененный список --> ", end="")
# for i in range(0,10):
#     print(src_list[i], end=" ")


""" 2.Напишите программу, в которой в списке целых чисел (заполненный
случайными числами в диапазоне от 0 до 10) нужно удалить элемент,
указанный пользователем.
Пример:
исходный список 3 1 6 3 8 5 6 2 8 9
укажите индекс элемента для удаления->4
измененный список 3 1 6 3 5 6 2 8 9 """

# import random

# src_list = []

# print("исходный список   --> ", end="")
# for i in range(0,10):
#     src_list.append(random.randint(0,10))
#     print(src_list[i], end=" ")

# item_index = int(input("\nукажите индекс элемента для удаления -> "))

# src_list.pop((item_index - 1))

# print("\nизмененный список --> ", end="")
# for i in range(0,10-1):
#     print(src_list[i], end=" ")

""" 3.Напишите программу, в которой создается список A1,A2, ...,An (заполненный
случайными числами в диапазоне от -9 до 10). He создавая дополнительные
списки, определить, какой из элементов повторяется в последовательности
A1,A2, ...,An наибольшее число раз.
Пример:
исходный список 1 4 -6 1 -3 -8 0 1 7 3
 чаще всего встречается элемент 1 """


# import random

# src_list = []

# n = 10

# print("исходный список   --> ", end="")
# for i in range(0,n):
#     src_list.append(random.randint(-9,10))
#     print(src_list[i], end=" ")

# max_count = 0
# for item in src_list:
#     count_item = src_list.count(item)
#     if count_item > max_count:
#         max_count = src_list.index(item)
# print("\nчаще всего встречается элемент ",src_list[max_count])


""" 4. Напишите программу, в которой создается список (заполненный случайными
числами в диапазоне от 1 до 10) целых чисел А. Нужно сдвинуть список А
циклически на т элементов вправо. При циклическом сдвиге вправо
выталкиваемые элементы с конца списка заполняют освобождающиеся места в
начале списка. Пример:
исходный список 3 1 6 3 8 5 6 2 8 9
укажите шаг сдвига ->4
измененный список 6 2 8 9 3 1 6 3 8 5  """

import random

src_list = []

n = 10

t = 4

print("исходный список   --> ", end="")
for i in range(0,n):
    src_list.append(random.randint(1,10))
    print(src_list[i], end=" ")

print("\n")
print("измененный список --> ", end="")

# Вычисляем позицию сдвигаемого элемента 
if t > n:
    pos = t - ((t // n) * n)
else:
    pos = n - t

# Сдвигаем элементы списка вправо от позиции сдвига до конца списка    
c = 0
res_list = []
while c < n:
    if c >= pos:
        res_list.append(src_list[c])
        c += 1
    else:
        c += 1
# Дописываем оставшиеся элементы списка в новый список
c = 0
while c < n:
    if c < pos:
        res_list.append(src_list[c])
        c += 1
    else:
        c += 1

# выводим полученный список        
for i in res_list:    
    print(i, end=" ")






# Проверять не надо. Это задачи с урока, я их делал тут чтобы не потерялись
# !--------------Задачи с занятия 17/06/2022-------------!
""" Домашнее задание: списки.
1. Напишите программу, в которой создается список из 10 элементов,
заполненный случайными числами в диапазоне от 0 до 5. Найти,
сколько в нем пар одинаковых соседних элементов.  """

# import random

# src_list = []
# print("исходный список   --> ", end="")
# for i in range(0,10):
#     src_list.append(random.randint(0,5))
#     print(src_list[i], end=" ")

# c_pair = 0
# item = 0  
# while item < len(src_list) - 1:
#     if src_list[item] == src_list[item+1]:
#         c_pair = c_pair + 1
#         item += 1
#     item += 1
# print("\nПар одинаковых элементов: ",c_pair)

""" 2.Написать программу, в которой в списке целых чисел, заполненный
случайными числами, заменить все элементы, меньшие среднего
арифметического, значением среднего арифметического, округленного до целого. 
 """

# import random

# src_list = []
# print("исходный список   --> ", end="")
# for i in range(0,10):
#     src_list.append(random.randint(0,9))
#     print(src_list[i], end=" ")


# sum = 0
# item = 0  
# while item < len(src_list) - 1:
#     sum = sum + src_list[item]
#     item += 1
# avg_list = round(sum / len(src_list))
# print("\nСреднее арифметическое: ", avg_list)

# item = 0
# while item < len(src_list) - 1:
#     if src_list[item] < avg_list:
#         src_list[item] = avg_list
#     item += 1


# print("\nизмененный список --> ", end="")
# for i in range(len(src_list)):
#     print(src_list[i], end=" ")

""" 3. Напишите программу, в которой создаются два списка целых чисел
размера n. Создать из них один список, в котором сначала идут отрицательные 
элементы, затем положительные, а затем нули. 
 """

# import random

# n = 10
# l1 = [random.randint(-5,5) for x in range(n)]
# l2 = [random.randint(-5,5) for x in range(n)]
# print(l1)
# print(l2)

# res = []

# v1
# for i in range(n):
#     if l1[i] < 0:
#         res.append(l1[i])
#     if l2[i] < 0:
#         res.append(l2[i])

# for i in range(n):
#     if l1[i] > 0:
#         res.append(l1[i])
#     if l2[i] > 0:
#         res.append(l2[i])

# for i in range(n):
#     if l1[i] == 0:
#         res.append(l1[i])
#     if l2[i] == 0:
#         res.append(l2[i])

# v2
# res =   [x for x in l1 if x < 0] + \
#         [x for x in l2 if x < 0] + \
#         [x for x in l1 if x > 0] + \
#         [x for x in l2 if x > 0]
# res += [0] * (n * 2 - len(res))
# print(res)

""" 4. Напишите программу, которая заполняет список из двадцати
элементов числами от 0 до 20 в случайном порядке. """

# import random
# l = [0 for x in range(20)]

# print(l)

# i = 0

# while i < len(l):
#     pos = random.randint(0,19)
#     if l[pos] == 0:
#         l[pos] = i
#         i += 1

# print(l)

   

    