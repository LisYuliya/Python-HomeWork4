# Вычислить число c заданной точностью d

import math

d = float(input('Введите число, с какой точностью необходимо вывести число Пи: '))
old = d
count = 0

while d % 1 > 0:
    d *= 10
    count += 1

p = math.pi
print(f'При точности {old} Пи равно: {str(round(p, count))}')

with open('pi.txt', 'a', encoding='utf-8') as file:
    file.write(f'При точности {old} Пи равно: {str(round(p, count))}'+'\n')
    file.close()