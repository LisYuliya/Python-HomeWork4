# Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

list = list(map(int, input('Введите числа через пробел:\n').split()))
print(f'Исходный список: {list}')
unique_list = []

for i in list:
    if i not in unique_list:
        unique_list.append(i)
print(f'Список из неповторяющихся элементов: {unique_list}')

with open('unique.txt', 'a', encoding='utf-8') as file:
    file.write(f'Из исходного списка {list} получается список неповторяющихся элементов: {unique_list}'+ '\n')
    file.close()