# Напишите программу, которая принимает на вход координаты двух точек и находит 
# расстояние между ними в 2D пространстве.

# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

import math

def distance_points(xa, xb, ya, yb):
    distance = math.sqrt((xa - xb)**2 + (ya-yb)**2)
    print(f'A({xa},{ya}); B({xb},{yb}) → {round(distance, 2)}')

xa = int(input('Введите координату x точки a: '))
ya = int(input('Введите координату y точки a: '))
xb = int(input('Введите координату x точки b: '))
yb = int(input('Введите координату y точки b: '))

distance_points(xa, xb, ya, yb)

