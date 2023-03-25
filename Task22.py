from random import randint

list_1 = [randint(0,100) for _ in range(int(input("Введите длину перового списка : ")))]
list_2 = [randint(0,100) for _ in range(int(input("Введите длину второго списка: ")))]

print(list_1)
print(list_2)

set_1 = set(list_1)
set_2 = set(list_2)

finall_list = list(set_1.intersection(set_2))

for i in range(len(finall_list)):
    min_value_index = i
    for j in range(i+1, len(finall_list)):
        if finall_list[j] < finall_list[min_value_index]:
            min_value_index = j
    finall_list[i], finall_list[min_value_index] = finall_list[min_value_index], finall_list[i]

print(finall_list)