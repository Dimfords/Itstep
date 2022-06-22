"""1. Найти:
а) все двузначные числа, сумма квадратов цифр которых делится на 13;
б) все двузначные числа, обладающие следующим свойством: если к
сумме цифр числа прибавить квадрат этой суммы, то получится снова
искомое число. """

# first_digit = 0
# second_digit = 0
# for i in range(10,100,1):
#     first_digit = i//10
#     second_digit = i - first_digit*10
#     if (first_digit**2 + second_digit**2)%13 == 0:
#         print ("а)",i)

# print("______\n")

# for i in range(10,100,1):
#     first_digit = i//10
#     second_digit = i - first_digit*10
#     if (first_digit + second_digit) + (first_digit + second_digit)**2 == i:
#         print ("б)",i)

""" 2. Найти все двузначные числа, которые делятся на n или содержат
цифру n. 
 """
# n = 8
# first_digit = 0
# second_digit = 0

# print("Делятся на n:")

# for i in range(10,100,1):
#     if i % n == 0:
#         print (i)

# print("\nСодержат цифру n:")

# for i in range(10,100,1):
#     first_digit = i//10
#     second_digit = i - first_digit*10
#     if first_digit == n or second_digit == n:
#         print (i)

""" 3.Найти:
а) все трехзначные числа, чьи квадраты оканчиваются тремя цифрами,
которые и составляют искомые числа;
б) все трехзначные числа, кратные семи и у которых сумма цифр также
кратна семи. """


# for i in range(100,1000,1):
#     last_3_digits_in_squere = (i**2) % 1000
#     if i == last_3_digits_in_squere:
#         print("а)",i)

# print("______\n")        

# for i in range(100,1000,1):
#     first_digit = i//100
#     second_digit = (i - first_digit*100)//10
#     third_digit = i - first_digit*100 - second_digit*10
#     if i % 7 == 0 and (first_digit + second_digit + third_digit) % 7 == 0:
#         print("б)",i)

""" 4. Найти сумму целых положительных чисел, больших 30 и меньших 100,
кратных трем и оканчивающихся на 2, 4 и 8.  """

# sum = 0
# for i in range(30,100,1):
#     first_digit = i//10
#     second_digit = i - first_digit*10
#     if i % 3 == 0: 
#         if second_digit == 2 or second_digit == 4 or second_digit == 8:
#             sum = sum + i
# print(sum)           

""" 5. Дано натуральное число:
а) Получить все его делители.
б) Найти сумму его делителей.
в) Найти сумму его четных делителей.
г) Определить количество его делителей.
д) Определить количество его нечетных делителей.
е) Определить количество его делителей. Сколько из них четных?
ж) Найти количество его делителей, больших d. """

# num = 72

# for i in range(num+1):
#     if i != 0 and num % i == 0:
#         print ("а)",i)

# print("______\n")

# sum = 0
# for i in range(num+1):
#     if i != 0 and num % i == 0:
#         sum = sum + i
# print ("б)",sum)

# print("______\n")

# sum = 0
# for i in range(num+1):
#     if i != 0 and num % i == 0 and i % 2 == 0:
#         sum = sum + i
# print ("в)",sum)

# print("______\n")

# c = 0
# for i in range(num+1):
#     if i != 0 and num % i == 0:
#         c = c + 1
# print ("г)",c)

# print("______\n")

# c = 0
# for i in range(num+1):
#     if i != 0 and num % i == 0 and i % 2 != 0:
#         c = c + 1
# print ("д)",c)

# print("______\n")

# c = 0
# for i in range(num+1):
#     if i != 0 and num % i == 0 and i % 2 == 0:
#         c = c + 1
# print ("е)",c)

# print("______\n")

# c = 0
# d = 10
# for i in range(num+1):
#     if i != 0 and num % i == 0 and i > d:
#         c = c + 1
# print ("ж)",c)

# print("\n")