# 3. Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N
#     *Примеры:*
#     - 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5

# N = abs(int(input()))
# for i in range(-N, N + 1):
#     print(i, end=" ")


N = abs(int(input()))
myList = [i for i in range(-N, N + 1)]
print(*myList, sep=", ")
