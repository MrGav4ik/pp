# Laboratorium: 04; Zadanie 06; Autor: Kudriavtsev Vitalii nr albumu 268940
# Oświadczam, że zadanie wykonałem samodzielnie.

height = input("Podaj wysokość trójkąta: ")

try:
    height = int(height) + 1

    if height > 1:
        for i in range(1, height):
            if i != (height):
                print("*" * i)
    if height <= 1:
        print("Podaj liczbę całkowitą dodatnią")

except ValueError:
    print("Podaj liczbę całkowitą dodatnią")
