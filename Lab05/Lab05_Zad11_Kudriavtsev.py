# Laboratorium: 05; Zadanie 11; Autor: Kudriavtsev Vitalii nr albumu 268940
# O�wiadczam, �e zadanie wykona�em samodzielnie.

text = input("Podaj dowonly tekst: ")
res = ""

print("podany tekst:", text)

text_no_space = text.replace(" ", "")

text_lower = text_no_space.lower()

for i in range(1, len(text_lower)+1):
    res += text_lower[-i]

if res == text_lower:
    print("Tekst jest palindromem")
else:
    print("Tekst NIE jest palindromem")