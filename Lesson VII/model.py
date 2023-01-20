x = 0
Y = 0


def init(a, b):
    global x
    global y
    x = a
    y = b


def addition():  # сложение
    return x + y


def subtraction():  # вычитание
    return x - y


def multiplication():  # умножение
    return x * y


def division():  # деление
    return x / y


def SearchingNumbers(task, place):
    first = 0
    for j in range(place - 1, -1, -1):
        if task[j] == '/' or task[j] == '*' or task[j] == '-' or task[j] == '+':
            first = j + 1
            break
    numberFirst = int(task[first:place])
    try:
        if task[first - 1] == "-":
            numberFirst = -int(task[first:place])
            first -= 1
    except:
        numberFirst = int(task[first:place])

    second = len(task)
    for j in range(place + 1, len(task)):
        if task[j] == '/' or task[j] == '*' or task[j] == '-' or task[j] == '+':
            second = j - 1
            break
    if second != len(task): second += 1
    numberSecond = int(task[place + 1:second])
    init(numberFirst, numberSecond)
    if task[place] == "*":
        rez = multiplication()
    elif task[place] == "/":
        rez = division()
    elif task[place] == "+":
        rez = addition()
    else:
        rez = subtraction()
    if rez < 0 and task[first-1] == '-':
        task = task[:first-1] + '+' + task[first + 1:]
    elif rez < 0 and task[first-1] != '-':
        task = task[:first-1] + '-' + task[first + 1:]
    rez = abs(rez)
    # Не работает если первое вычисляемое число становится отрицательным
    return task[0:first] + str(rez) + task[second:len(task)]
