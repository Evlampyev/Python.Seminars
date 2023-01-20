from datetime import datetime


def log_input(data):
    time = datetime.now().strftime('%H:%M')
    with open('log.csv', 'a') as file:  # Открытие для добавления
        file.write('{}; {} ='
                   .format(time, data))

def log_result (data):
    with open('log.csv', 'a') as file:  # Открытие для добавления
        file.write('{}; \n'
                   .format(data))
