import controller

academic_discipline = ['Русский язык', 'Математика', 'Информатика']


def tearcher_work(discipline):
    path = academic_discipline[discipline] + '.txt'
    try:
        with open(path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
    except:
        with open(path, 'w+', encoding='utf-8') as file:
            lines = file.readlines()
    print("---Список учеников---")
    print("Укажите порядковый номер ученика: ")
    for i in range(len(lines)):
        lst = lines[i].split()
        print(f"{i + 1}. {lst[0]}")
    print(f"{i + 2}. Ученика нет. Добавить. ")
    count = int(input("Ваш выбор: "))
    if count == len(lines) + 1:
        student_add(discipline)
    else:
        mark_add(discipline, i)
    return


def student_add(discipline):
    print("---Новый ученик---")
    student = input("Укажите фамилию ученика: ")
    mark = input("Какую отметку вы хотите поставить: ")
    path = academic_discipline[discipline] + '.txt'
    with open(path, 'a', encoding="utf-8") as file:
        file.write(f"{student} {mark}\n")
    return


def mark_add(discipline, student):
    # читать все, заменить и переписать файл
    return
