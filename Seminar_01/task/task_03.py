#Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
x=int(input('input x: '))
y=int(input('input y: '))
if x>0 and y>0: print(1)
elif x<0 and y>0: print(2)
elif x<0 and y<0: print(3)
elif x>0 and y<0: print(4)
else: print('x и y не должны быть = 0')