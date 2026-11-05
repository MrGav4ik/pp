# Laboratorium: 05; Zadanie 04; Autor: Kudriavtsev Vitalii nr albumu 268940
# Oświadczam, że zadanie wykonałem samodzielnie.

text = "Ala ma koty"
number = 2
res = ""

words = text.split(" ")

for i in range(0, len(words)):
    if i != 2:
        print(words[i])
    else:
        print(number)
        print(words[i])