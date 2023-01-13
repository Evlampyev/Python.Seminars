# 1) В файле находится N натуральных чисел, записанных через пробел. Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.

with open('1.txt', 'r') as data:
    all = list(map(int, data.readline().split()))
print(all)

n = len(all) - 1
while (all[n] - 1 == all[n - 1]):
    n -= 1
print(all[n] - 1)
