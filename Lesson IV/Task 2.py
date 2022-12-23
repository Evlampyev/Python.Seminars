# Решить квадратное уравнение

a, b, c = map(int, input("Введите коэффициенты a,b,c через пробел ").split())
D = b ** 2 - 4 * a * c
if D < 0:
    print("Корней нет")
elif D == 0:
    print(f"x = {-b/(2*a)}")
else:
    print(f'x1 = {(-b+D**0.5)/(2*a)}')
    print(f'x2 = {(-b-D**0.5)/(2*a)}')

