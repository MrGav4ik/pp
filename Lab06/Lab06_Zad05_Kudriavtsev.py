# Laboratorium: 06; Zadanie 05; Autor: Kudriavtsev Vitalii nr albumu 268940
# O�wiadczam, �e zadanie wykona�em samodzielnie.

words = {}

sentance = input("Podaj zdanie: ")

for i in sentance.split(" "):
    if i in words.keys():
        words[i.lower()] += 1
    else:
        words[i.lower()] = 1

for i, j in words.items():
    print(f"{i}: {j}")