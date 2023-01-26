from user_interface import (tearcher, stydent)


def initial():
    choose = 0
    print("+++ ГЛАВНОЕ МЕНЮ +++")
    print("1. Учитель")
    print("2. Ученик")
    print("3. Выход")
    while (True):
        choose = int(input("Вам куда? "))
        if choose == 1:
            tearcher()
        elif choose == 2:
            stydent()
        else:
            break
