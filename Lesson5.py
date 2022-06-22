""" Задание 1 ( то, что не доделали на уроке)
#-------------------
Написать программу, которая будет принимать на через консоль текст
И будет возвращать первые 3 символа, но в обратном порядке

Пример 1:
Если мы ввели "Example"
То программа вернет "axE"

При этом если пользователь ввел что то короче 3х символов, 
то недостающие символы должны быть заменены "*"

Пример 2:
Если мы ввели только "E"
недостающие числа были заменены на *
Поэтому первые три символа теперь "E**"
После разворота
Программа вернет "**E"

Пример 3:
Мы ничего не ввели иными словами ввели ""
Программа присвоит первым 3 символам значение *
И вернет "***"

Используйте конструкцию(и) try except в программе """

#Uncomment to run
""" tx = input("Введите текст:")
try:
        ch = tx[0]
except IndexError:
        print('*'+'*'+'*')
else:
    try:
            ch = tx[1]
    except IndexError:
            print('*'+'*'+tx[0])
    else:
        try:
            ch = tx[2]
        except IndexError:
            print('*'+tx[1]+tx[0])
        else:
            print(tx[2]+tx[1]+tx[0]) """
                


""" Задание 2
#-------------------
Написать программу, которая будет делить одно число на другое
Но, если случиться, что делить нужно на ноль, программа заменит ноль на 
стремящееся к нулю число
например 0.00000000000000000000001
И вернет результат вычислений
Используйте конструкцию(и) try except в программе
 """

#Uncomment to run
""" x = 1
y = 0

try:
    print(x/y)
except ZeroDivisionError:
    print(x/0.00000000000000000000001)

 """

""" Задание 3
#-------------------
Напишите программу - калькулятор, который может работать в двух режимах:
Конкатенации строк и арифметического сложения чисел 
Пользователь вводит 2 числа и способ, которым он хочет сложить данные

Обработать ошибку, которая может возникнуть, 
выведя принт с текстом "произошла ошибка:" и далее вставить название ошибки

*Для того что бы достать название ошибки, используйте выражение ошибки через "as"
Напоминаю, как єто сделать:
# except Exception as ex:
#     print(ex.__class__)
 """


#Uncomment to run
""" method = input("Введите способ для сложения данных: конкатенация(конк) строк или сложение(слож):")
if method == "слож":
    while True:
        x = input("Введите число1:")
        y = input("Введите число2:")
        try:
           float(x)
           float(y)
        except Exception as ex:
         print("Вы ввели вместо числа - текст",ex.__class__)
        else:
         print(float(x)+float(y))   
         break
elif method == "конк":
        x = input("Введите текст1:")
        y = input("Введите текст2:")
        print(x+y)
else:
    print("Введите или 'слож' или 'конк'") """


""" Задание 4 (со звездочкой *)
#-------------------
Написать программу, которая принимает ввод от пользователя и проверяет его по нескольким критериям
Если 2 или более критериев не совпадает - нужно "поднять" ошибку ValueError
И обработать ее принтом ("2 условия не было выполнено")

Условия:
1. Если введены данные, которые можно привести к численному типу, то их значение должно быть менее 15
2. Длинна в пределах между 3 и 7 символами
3. Если введены данные, которые НЕЛЬЗЯ привести к численному типу, то в них должны содержаться
 все из перечисленных символов "b", "x", "3"
 """

#Нужна помощь. Не осилил :)

data = input("Введите данные:")
try:
    float(data) 
    if float(data) < 15:
        print ("Условие 1 выполнено!")
    else:
            try:
                float(data) 
            except ValueError:
                if len(data) >= 3 and len(data) <= 7:
                    print ("Условие 2 выполнено!")
                elif "b" in data and "x" in data and "3" in data:
                    print ("Условие 3 выполнено!")
            finally:
                raise ValueError('2 условия не было выполнено')
except ValueError:
    try:
        float(data) 
    except ValueError:
        if len(data) >= 3 and len(data) <= 7:
            print ("Условие 2 выполнено!")
        elif "b" in data and "x" in data and "3" in data:
            print ("Условие 3 выполнено!")
        else:
            raise ValueError('2 условия не было выполнено')

    