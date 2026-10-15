# Laboratorium: 03; Zadanie 02; Autor: Kudriavtsev Vitalii nr albumu 262516
# Oświadczam, że zadanie wykonałem samodzielnie.

liczba1 = int(input("Wprowadź pierwszą liczbę w zakresie 1-100: "))
liczba2 = int(input("Wprowadź drugą liczbę w zakresie 1-100: "))

if (liczba1 < 1 or liczba1 > 100) or (liczba2 < 1 or liczba2 > 100):
    print("Liczba nie należy do zakresu")
else:
    if liczba1 % liczba2 == 0:
        print("Pierwsza liczba jest podzielna przez drugą bez reszty")
    else:
        print("Pierwsza liczba NIE jest podzielna przez drugą bez reszty")