# Напишите программу, которая по заданному номеру четверти, показывает диапазон 
# возможных координат точек в этой четверти (x и y).



def coordinate_range(n):
    if n <1 or n > 4:
        return print('Введите число от 1 до 4')
    elif n == 1:
        return print('x > 0 and y > 0')
    elif n == 2:
        return print('x < 0 and y > 0')
    elif n == 3:
        return print('x < 0 and y < 0')
    elif n == 4:
        return print('x > 0 and y < 0')

n = int(input('Введите номер четверти: '))
coordinate_range(n)















