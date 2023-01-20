def SearchingNumbers(task, place):
    first = 0
    for j in range(place - 1, -1, -1):
        if task[j] == '/' or task[j] == '*' or task[j] == '-' or task[j] == '+':
            first = j + 1
            break
    numberFirst = int(task[first:place])
    second = len(task)
    for j in range(place + 1, len(task)):
        if task[j] == '/' or task[j] == '*' or task[j] == '-' or task[j] == '+':
            second = j - 1
            break
    if second != len(task): second += 1
    numberSecond = int(task[place + 1:second])
    if task[place] == "*":
        rez = numberFirst * numberSecond
    elif task[place] == "/":
        rez = int(numberFirst / numberSecond)
    elif task[place] == "+":
        rez = numberFirst + numberSecond
    else:
        rez = numberFirst - numberSecond

    return task[0:first] + str(rez) + task[second:len(task)]


expression = '5*2+67*2+2-6/2'
print(expression, '= ', end="")

operations = ['/', '*', '+', '-']
for i in range(4):
    while expression.find(operations[i]) > 0:
        operat = expression.find(operations[i])
        expression = SearchingNumbers(expression, operat)
print(expression)
