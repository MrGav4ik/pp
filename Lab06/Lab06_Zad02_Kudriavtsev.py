# Laboratorium: 06; Zadanie 02; Autor: Kudriavtsev Vitalii nr albumu 268940
# O�wiadczam, �e zadanie wykona�em samodzielnie.

books = {}

for i in range(1, 4):
    title = input(f"Podaj tytuł książki nr {i}: ")
    author = input("Podaj autora: ")
    books[title] = author

print("Lista wprowadzonych książek:")

for i, j in books.items():
    print(f'"{i}": autor: {j}')