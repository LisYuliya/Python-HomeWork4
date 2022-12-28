# Задайте натуральное число N.
# Напишите программу, которая составит список простых множителей числа N.


num = int(input("Введите число: "))
i = 2  # первое простое число
list = []
num1 = num
while i <= num:
    if num % i == 0:
        list.append(i)
        num //= i
        i = 2
    else:
        i += 1
print(f"Простые множители числа {num1}: {list}")

with open('factor-n.txt', 'a', encoding='utf-8') as file:
    file.write(f'Простые множители числа {num1}: {list}'+ '\n')
    file.close()