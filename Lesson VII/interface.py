# Вводит с клавиатуры и отправляет в логгирование
import logger as log


def entering_tasks():
    data = input('Entering tasks: ')
    log.log_input(data)
    return data
