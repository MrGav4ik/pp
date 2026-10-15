# Laboratorium: 03; Zadanie 01; Autor: Kudriavtsev Vitalii nr albumu 262516
# Oświadczam, że zadanie wykonałem samodzielnie.

day_number = int(input("Wprowadź numer dnia tygodia (1-7): "))

days = [
    "Poniedziałek",
    "Wtorek",
    "Środa",
    "Czwartek",
    "Piątek",
    "Sobota",
    "Niedziela"
]


if day_number >= 1 and day_number <= len(days):
    print(days[day_number - 1])