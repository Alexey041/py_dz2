#1
""" Напишите программу, которая принимает на вход вещественное число и показывает
сумму его цифр.
- 6782 -> 23
- 0,56 -> 11 """

some_str = input('Введите вещественное число: ')
sum = 0
for i in some_str:
    if i != '.':
        sum += int(i)

print(sum)

#2
""" Напишите программу, которая принимает на вход число N и выдает набор
произведений чисел от 1 до N.
- пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4) """

num = int(input('Введите число: '))
f = 1
some_list = []
for i in range(1, num + 1):
    f = f * i
    some_list.append(f)
print(some_list)

#3
""" Задайте список из n чисел последовательности (1 + 1 / n) ** n и выведите на
экран их сумму.
Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19} """

n = int(input('Введите число: '))
sum = 0
some_list = []
for i in range(1, n + 1):
    sum += (1 + 1 / i) ** i
    some_list.append(f'{i}: {round(sum, 2)}')

print(some_list)

#4
#Реализуйте алгоритм перемешивания списка

some_list = [2, 4, 5, -1]
import random
random.shuffle(some_list)
print(some_list)