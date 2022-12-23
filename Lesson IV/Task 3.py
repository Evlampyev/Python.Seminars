# Найти НОК двух чисел

a, b = map(int, input("Введите два числа через пробел ").split())
Nok = a * b
print(f'НОК ({a},{b}) = ', end="")
limit = max(a, b)
limit = round(limit ** 0.5)
i = 2
while i < limit + 1:
    if a % i == 0 and b % i == 0:
        a = a // i
        b = b // i
        Nok = Nok // i
    else:
        i += 1
print(Nok)
