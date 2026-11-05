# Laboratorium: 05; Zadanie 10; Autor: Kudriavtsev Vitalii nr albumu 268940
# O�wiadczam, �e zadanie wykona�em samodzielnie.

name = input("Podaj Imię: ")
surname = input("Podaj Nazwisko: ")
number = input("Podaj numer telefonu: ")

if name.isalpha():
    print("Imię składa się wyłącznie z liter")
else:
    print("Imię NIE składa się wyłącznie z liter")

if surname.isalpha():
    print("Nazwisko składa się wyłącznie z liter")
else:
    print("Nazwisko NIE składa się wyłącznie z liter")

if number.isdigit():
    print("Numer telefonu składa się wyłącznie z cyfr")
else:
    print("Numer telefonu NIE składa się wyłącznie z cyfr")