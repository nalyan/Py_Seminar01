#Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

week = [1,2,3,4,5,6,7]
day=int(input('введите номер дня недели: '))
for i in range(6):
  if day==int(week[i]):
    check=True
    break
  else:
    check=False
if (day==6 or day==7):
  print('это выходной')
elif check==True:
  print('это не выходной')
else: print('нет такого дня')