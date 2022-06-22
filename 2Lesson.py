""" Задание 1
Пользователь вводит с клавиатуры три цифры. Необходимо создать число, содержащее эти цифры. Например,
если с клавиатуры введено 1, 5, 7, тогда нужно сформировать число 157. """

#Uncomment for cheking
""" a = input("Input 1st digit:")
b = input("Input 2nd digit:")
c = input("Input 3rd digit:")

print("result is:",a+b+c) """


""" Задание 2
Пользователь вводит с клавиатуры число, состоящее
из четырех цифр. Требуется найти произведение цифр.
Например, если с клавиатуры введено 1324, тогда результат произведения 1*3*2*4 = 24. """

#Uncomment for cheking
""" a = int(input("Input 1st int digit:"))
b = int(input("Input 2nd int digit:"))
c = int(input("Input 3rd int digit:"))
d = int(input("Input 4rd int digit:"))

print("Result of multiplying is:",a*b*c*d) """

""" Задание 3
Пользователь вводит с клавиатуры количество метров.
Требуется вывести результат перевода метров в сантиметры, дециметры, миллиметры, мили. """

#Uncomment for cheking
""" meters = int(input("Please input meters (int):"))
print ("Santimeters:",meters*100)
print("Decimeters:",meters*10)
print("Milimeters:",meters*1000)
print("Miles:",meters/1000/1.61) """


""" Задание 4
Напишите программу, вычисляющую площадь треугольника. Пользователь с клавиатуры вводит размер
основания треугольника и размер высоты. """

#Uncomment for cheking
""" height = float(input("Please input height (float):"))
triangle_base = float(input("Please input triangle base (float):"))
print("Triangle area is:",1/2*height*triangle_base) """


""" Задание 5 (задача со звездочкой*)
Пользователь с клавиатуры вводит четырёхзначное
число. Необходимо перевернуть число и отобразить
результат. Например, если введено 4512, результат 2154. """

#Uncomment for cheking (I use slice  [start:stop:step])

n = input('Input 4 digit number: ')[::-1]
print(n)