# Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
# в которой находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

print("Ввведите коодинату по оси Х:  ")
x = float(input())

print("Ввведите коодинату по оси Y:  ")
y = float(input())

if (x > 0 and y > 0):
    print("1 четверть")
if (x < 0 and y > 0):
    print("2 четверть")
if (x < 0 and y < 0):
    print("3 четверть")
if (x > 0 and y < 0):
    print("4 четверть")
