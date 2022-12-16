# 5 мест по росту, шестого куда ставить.
array = [172, 170, 167, 165, 160]
nextMen = int(input())
count = 0
for i in range(0, len(array)):
    if array[i] > nextMen:
        count += 1
print(count + 1)
