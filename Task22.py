# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества.
# m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

from random import randint
setM = set(randint(1, 50) for i in range(int(input("Введите кол-во элементов первого множества: "))))
print(setM)
setN = set(randint(1, 50) for i in range(int(input("Введите кол-во элементов второго множества: "))))
print(setN)
setSort = sorted(setN.intersection(setM))
print(*setSort)
