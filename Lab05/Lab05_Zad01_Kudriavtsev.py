# Laboratorium: 05; Zadanie 01; Autor: Kudriavtsev Vitalii nr albumu 268940
# Oświadczam, że zadanie wykonałem samodzielnie.


text = input("Wpisz dowolny tekst: ")
text_len = len(text)
middle_leter = int(text_len / 2)

print(text)
print("Liczba znaków jest równa:", text)
print("Pierwszy znak:", text[0])
print("Ostatni znak:", text[-1])

if text_len % 2 == 0:
    print("Środkowe znaki:", text[middle_leter-1:middle_leter+1])
else:
    print("Środkowe znaki:", text[middle_leter-1:middle_leter+2])