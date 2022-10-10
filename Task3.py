# Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка 
# (или на какой оси она находится).

# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3



def quarter_number(x,y):
    if x > 0 and y > 0:
        return print(f'x={x}; y={y} → 1')
    elif x < 0 and y > 0:
        return print(f'x={x}; y={y} → 2')
    elif x < 0 and y < 0:
        return print(f'x={x}; y={y} → 3')
    elif x > 0 and y < 0:
        return print(f'x={x}; y={y} → 4')
        
x = int(input('Введите чило х: '))
y = int(input('Введите чило y: '))
quarter_number(x,y)














