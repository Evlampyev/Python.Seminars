from interface import entering_tasks
from model import SearchingNumbers
from view import *


def process_data():
    expression = task = entering_tasks()  # вызов ввода
    operations = ['/', '*', '-', '+']
    step = 0
    for i in range(4):
        while expression.find(operations[i]) > 0:
            operat = expression.find(operations[i])
            expression = SearchingNumbers(expression, operat)
            step += 1
            print_step(expression, step)
    print_result(task, expression)  # вызов вывода
