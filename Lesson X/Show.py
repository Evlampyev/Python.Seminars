from random import choice


def init_pole():
    board = ['👁', '👁', '👁', '👁', "🤡", "🤡", "🤡", "🙈", "🙈", '❤']
    lst = [choice(board) for i in range(12)]
    return lst


def calculation_of_winnings(lst):
    coefficient = 0
    coef_dict = {
        '👁': [1.5, 1],
        '🤡': [2.5, 2],
        '🙈': [3.5, 3],
        '❤': [5.0, 4]
    }
    print(lst)
    for i in range(len(lst), 4):
        if lst[i] == lst[i + 1] == lst[i + 2] == lst[i + 3]:
            coefficient += coef_dict[lst[i]][0]
    print('1-', coefficient)
    for i in range(len(lst) // 3):
        if lst[i] == lst[i + 4] == lst[i + 8]:
            coefficient += coef_dict[lst[i]][1]
    print('2-', coefficient)
    return coefficient


def output_board(lst):
    text = ""
    for i in range(len(lst)):
        if i % 4 < 3:
            text = text + str(lst[i]) + '-'
        else:
            text = text + str(lst[i]) + '\n'
    return text
