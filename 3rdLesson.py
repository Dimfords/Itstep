""" a = int(input("Input number A:"))
b = int(input("Input number B:"))
c = 0

try:
    c = a/b
 
except ZeroDivisionError:
     print("You are dividing by zero!")

finally:
    print("Result of dividing is:",c)
 """

 
myStr="Python was created in the late 1980's by Guido van Rossum."
print(myStr.count('Python')) #2
print(myStr.count('Python',0,-50)) #1
print(myStr.count('Python',10)) #1