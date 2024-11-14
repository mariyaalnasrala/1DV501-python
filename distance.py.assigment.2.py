# skapa en funktion
import math


def distance_between(x1, y1, x2, y2):
    distance = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    return distance


x1_koor = float(input('Enter x1 '))
y1_koor = float(input('Enter y1 '))
x2_koor = float(input('Enter x2 '))
y2_koor = float(input('Enter y2 '))

print(f'The distance between{x1_koor, y1_koor} and {x2_koor, y2_koor} is')
print(round(distance_between(x1_koor, y1_koor, x2_koor, y2_koor), 3))
