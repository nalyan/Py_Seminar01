#Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D

import math
print('введите координаты точек: ')
x1=int(input('x1: '))
y1=int(input('y1: '))
x2=int(input('x2: '))
y2=int(input('y2: '))
print(round(math.sqrt(abs((x2-x1)**2 + (y2-y1)**2)),2))