from database import academic_discipline
from database import tearcher_work
import controller


def tearcher():
    print("---УЧИТЕЛЬ---")
    print('По какому предмету хотите поставить отметку?')
    for i in range(len(academic_discipline)):
        print(f"{i + 1}. {academic_discipline[i]}")
    disc = int(input("Ваш выбор: ")) - 1
    tearcher_work(disc)
    print('------------')
    print('1. Выбрать другой предмет')
    print('2. Вернуться в меню выбора пользователя')
    menu = 0
    while menu != 1 or menu != 2:
        menu = int(input("Ваш выбор: "))
        if menu == 1:
            tearcher()
            break
        elif menu == 2:
            controller.initial()
            break
        else:
            print("Повторите ввод")


def stydent():
    return
