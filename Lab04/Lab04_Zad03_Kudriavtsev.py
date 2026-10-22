# Laboratorium: 04; Zadanie 03; Autor: Kudriavtsev Vitalii nr albumu 268940
# Oświadczam, że zadanie wykonałem samodzielnie.

n = int(input("Podaj liczbę całkowitą n z zakresu 1..10: "))

numbers = []

for i in range(1, 10):
    numbers.append(i)

if n in numbers:
    for i in numbers:
        print(f"{n} * {i} =  {n * i}")
else:
    print("Podana liczba nie należy do zakresu")