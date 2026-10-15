# Laboratorium: 03; Zadanie 04; Autor: Kudriavtsev Vitalii nr albumu 262516
# Oświadczam, że zadanie wykonałem samodzielnie.

year = int(input("Wprowadź rok(np. 2026): "))

if year % 4 == 0 and year % 100 != 0:
    print("Rok jest przestępny")
else:
    print("Rok NIE jest przestępny")