# 1.Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.

import random

myArray = [random.randint(0, 15) for i in range(10)]
search = int(input("Введите искомое число "))
print(f"Исходный список: {myArray}")
# yes = False
# i = 0
# while not (yes) and i < 10:
#     if myArray[i] == search:
#         yes = True
#     else:
#         i += 1
# print(yes)

if search in myArray:
    print(True)
else:
    print(False)
