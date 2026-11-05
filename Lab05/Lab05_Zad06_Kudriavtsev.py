# Laboratorium: 05; Zadanie 06; Autor: Kudriavtsev Vitalii nr albumu 268940
# Oświadczam, że zadanie wykonałem samodzielnie.

text = "Ala ma 2 koty"

if text.islower() == False:
    print(text)
    text_lower = text.lower()
    print(text_lower)
    text_capital = text_lower[:0] + text_lower[0].upper() + text_lower[1:]
    print(text_capital)