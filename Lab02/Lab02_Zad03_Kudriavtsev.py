# Laboratorium: 02; Zadanie 03; Autor: Kudriavtsev Vitalii nr albumu 262516
# Oświadczam, że zadanie wykonałem samodzielnie.

import math

x = list(input("Podaj współrzędne pierwszego punktu na płaszczyźnie (np. 2 1): "))
y = list(input("Podaj współrzędne drugiego punktu na płaszczyźnie (np. 1 2): "))

distance = math.sqrt((int(x[2])-int(x[0]))**2+(int(y[2])-int(y[0]))**2)

print("Odległość między tymi punktami wynosi:", distance)