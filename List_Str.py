""" Модуль 4. Строки. Списки.
Часть 3
Задание 1
Два списка целых заполняются случайными числами.
Необходимо:
■ Сформировать третий список, содержащий элементы
обоих списков;
■ Сформировать третий список, содержащий элементы
обоих списков без повторений;
■ Сформировать третий список, содержащий элементы
общие для двух списков;
■ Сформировать третий список, содержащий только
уникальные элементы каждого из списков;
■ Сформировать третий список, содержащий только
минимальное и максимальное значение каждого из
списков. """


import random

from numpy import append

src_list_1 = []
src_list_2 = []

# Размер списков
n = 10

print("исходный список 1   --> ", end="")
for i in range(0,n):
    src_list_1.append(random.randint(0,10))
    print(src_list_1[i], end=" ")

print("\n")
print("исходный список 2   --> ", end="")

for i in range(0,n):
    src_list_2.append(random.randint(0,10))
    print(src_list_2[i], end=" ")

print("\n")

print("■ Сформировать третий список, содержащий элементы  обоих списков:")

res_list = []
c = 0
while c <= n -1:
    res_list.append(src_list_1[c])
    c += 1
c = 0
while c <= n -1:
    res_list.append(src_list_2[c])
    c += 1


# выводим полученный список    
for i in res_list:
    print(i, end=" ")

print("\n")

print("■ Сформировать третий список, содержащий элементы обоих списков без повторений:")

res_list = []

for i in src_list_1:
    for j in src_list_2:
        if i == j:
            if i not in res_list: # убираем повторения
                res_list.append(i)

# выводим полученный список    
for i in res_list:
    print(i, end=" ")

print("\n")

# print("■ Сформировать третий список, содержащий элементы общие для двух списков:")

# res_list = []

# for i in src_list_1:
#     try:
#         if src_list_2.index(i) >= 0 :
#             res_list.append(i)
#     except: ValueError
     


# # выводим полученный список    
# for i in res_list:
#     print(i, end=" ")

print("\n")

print("■ Сформировать третий список, содержащий только уникальные элементы каждого из списков;")

res_list = []
temp_list = []
for i in src_list_1:
    if i not in temp_list:
        temp_list.append(i)
        res_list.append(i)
temp_list = []
for i in src_list_2:
    if i not in temp_list:
        temp_list.append(i)
        res_list.append(i)

# выводим полученный список    
for i in res_list:
    print(i, end=" ")

print("\n")
print("Сформировать третий список, содержащий только минимальное и максимальное значение каждого из списков. ")

res_list = []
temp_list = []

max1 = max(src_list_1)
min1 = min(src_list_1)

max2 = max(src_list_2)
min2 = min(src_list_2)

res_list = [max1, min1, max2, min2]

# выводим полученный список    
for i in res_list:
    print(i, end=" ")