# Найти НОК двух чисел: Алгоритм Евклида
a, b = map(int, input("Введите два числа через пробел ").split())
s = a * b
a, b = max(a, b), min(a, b)
while a != 0 and b != 0:
    a, b = b, a % b
print(f'НОД = {b + a}')
print((f'НОК = {s // (b + a)}'))
