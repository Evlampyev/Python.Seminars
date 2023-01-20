# Выводит на экран

def print_result(initial, rezult):
    print("======================")
    print(f'{initial} = {rezult}')
    print("======================")

    with open('log.csv', 'a') as file:
        file.write('{} \n'
                   .format(rezult))


def print_step(rezult, step=0):
    print(f'step = {step}: {rezult}')
