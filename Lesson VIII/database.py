academic_discipline = ['Русский язык', 'Математика', 'Информатика']


def tearcher_work(discipline):
    path = academic_discipline[discipline] + '.txt'
    try:
        with open(path, 'r', encoding='windows-1251') as file:
            lines = file.readlines()
    except:
        with open(path, 'w+', encoding='windows-1251') as file:
            lines = file.readlines()
    print("---Список учеников---")
    print("Укажите порядковый номер ученика: ")
    i = -1
    for i in range(len(lines)):
        lst = lines[i].split()
        print(f"{i + 1}. {lst[0]}")
    print(f"{i + 2}. Ученика нет. Добавить. ")
    count = input("Ваш выбор: ")
    while not (count.isdigit()) or int(count) > i + 2:
        count = input("Повторите ввод: ")
    if int(count) == i + 2 or (int(count) - 2 == -1 and i == -1):
        student_add(discipline)
    else:
        mark_add(discipline, int(count))


def student_add(discipline):
    print("---Новый ученик---")
    student = input("Укажите фамилию ученика: ")
    mark = input("Какую отметку вы хотите поставить: ")
    path = academic_discipline[discipline] + '.txt'
    with open(path, 'a', encoding="windows-1251") as file:
        file.write(f"{student} {mark}\n")
    return


def mark_add(discipline, student):
    path = academic_discipline[discipline] + '.txt'
    with open(path, 'r+', encoding='windows-1251') as file:
        lines = file.readlines()
    i = 1
    new_lines = str()
    for line in lines:
        if i == student:
            lst = line.split()
            mark = input(f"Какую оценку ставим {lst[0]}: ")
            lst.append(mark)
            str_lst = " ".join(lst)
            print(str_lst)
            line = str_lst + '\n'
        new_lines = new_lines + line
        i += 1
    with open(path, 'w') as file:
        file.write(new_lines)
