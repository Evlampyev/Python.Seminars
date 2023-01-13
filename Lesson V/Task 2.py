# 2) Написать программу, которая будет удалять все слова в которых есть "абв"
# Ввод: привет приаб приабвет
# Вывод: привет приаб


def DeliteWord(lst: list[str], key: str = 'абв'):
    res_lst = []
    for i in lst:
        if key not in i:
            res_lst.append(i)
    return res_lst


line = 'Привет ,абырвал, пабв капабпв пжжабв'
line = line.split()
print(line)
print(DeliteWord(line))

