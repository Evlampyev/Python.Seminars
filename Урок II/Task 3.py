# 3) Петя и катя - брат и сестра. Петя - студент, а Катя - школьница. Петя помогает Кате по математике.
# Он задумывает два натуральных числа, а Катя должна их отгадать
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P
# Помогите Кате отгадать задуманные Петей числа.
# *Пример*
# Ввод: 4 4
# Вывод: 2 2
# *Пример*
# Ввод: 5 6
# Вывод: 2 3


summation, composition = map(int, input().split())
limit = summation
if summation < composition:
    limit = composition
for i in range(0, limit + 1):
    if (summation - i) * i == composition:
        print(summation - i, i)
        break
