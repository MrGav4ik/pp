# Laboratorium: 06; Zadanie 06; Autor: Kudriavtsev Vitalii nr albumu 268940
# O�wiadczam, �e zadanie wykona�em samodzielnie.

words1 = set()
words2 = set()

sentance1 = input("Podaj pierwsze zdanie: ")
sentance2 = input("Podaj drugie zdanie: ")

for i in sentance1.split(" "):
    words1.add(i.lower())

for i in sentance2.split(" "):
    words2.add(i.lower())

intersection = words1 & words2
difference = words1 - words2
union = words1 | words2


print("Słowa występujące w obu zdaniach:", intersection if intersection else "Brak słow")
print("Słowa występujące tylko wpierwszym zdaniu:", difference if difference else "Brak słow")
print("Wszystkie różne słowa z obu zda:", union if union else "Brak słow")
