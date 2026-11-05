# Laboratorium: 05; Zadanie 08; Autor: Kudriavtsev Vitalii nr albumu 268940
# O�wiadczam, �e zadanie wykona�em samodzielnie.

text = input("Wpisz dowolny tekst: ")
width = int(input("Podaj szerokość pola (liczba całkowita): "))

res = text.rjust(width, "*")

print(res)