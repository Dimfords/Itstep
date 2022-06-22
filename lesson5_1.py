
# 
h = 53
while True:
    figure_type = input("Выберите фигуру из списка: б, и,а:")
    if figure_type == "б":
        # б
        for i in range(0,20,1):
            print ("*"*i)
    elif figure_type == "а":
            # а
        for i in range(0,20,1):
            print (" "*i+(20-i)*"*")
    elif figure_type == "к":
            # к
        for i in range(20,0,-1):
            print (" "*i+(20-i)*"*")
    elif figure_type == "г":
            # г
        for i in range(h):
            print(" "*(h-1-i) + "* "*(i+1) + " "*(h-2-i))
    elif figure_type == "в":
            # в
        for i in range(h-1,-1,-1):
            print(" "*(h-1-i) + "* "*(i+1) + " "*(h-2-i))
        for i in range(h):
            print(" "*h)
    elif figure_type == "г":
        for i in range(h):
            print(" "*h)
        for i in range(h):
            print(" "*(h-1-i) + "* "*(i+1) + " "*(h-2-i))
    elif figure_type == "д":
        for i in range(h-1,-1,-1):
            print(" "*(h-1-i) + "* "*(i+1) + " "*(h-2-i))
        for i in range(h):
            print(" "*(h-1-i) + "* "*(i+1) + " "*(h-2-i))
    elif figure_type == "е":
        for i in range(h):
            print("*"*i + " "*(h-i) + " "*(h-i) + "*"*i)
        for i in range(h,0,-1):
            print("*"*i + " "*(h-i) + " "*(h-i) + "*"*i)
    elif figure_type == "ж":
        for i in range(h):
            print("*"*i + " "*(h-i))
        for i in range(h,0,-1):
            print("*"*i + " "*(h-i))
    elif figure_type == "з":
        for i in range(h):
            print(" "*(h-i) + "*"*i)
        for i in range(h,0,-1):
            print(" "*(h-i) + "*"*i)
    elif figure_type == "и":
            # и
        for i in range(20,0,-1):
            print ("*"*i)
    else:
        print("Ошибочный выбор! Перезапустите программу.")
        break