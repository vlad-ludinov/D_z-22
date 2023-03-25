from random import randint


bushes = [randint(0, 20) for _ in range(int(input("Введите количество кустов: ")))]

collect_berries = []

print(f"Количество ягод на кустах: {bushes}")

for i in range(len(bushes)-1):
    collect_berries.append(bushes[i-1]+bushes[i]+bushes[i+1])
collect_berries.append(bushes[len(bushes)-2]+bushes[len(bushes)-1]+bushes[0])
print(f"Возможные варианты сбора: {collect_berries}")

max_collect = collect_berries[0]
for i in collect_berries:
    if i > max_collect:
        max_collect = i
print(f"Максимально число ягод которое можно собрать: {max_collect}")