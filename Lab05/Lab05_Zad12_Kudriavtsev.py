# Laboratorium: 05; Zadanie 12; Autor: Kudriavtsev Vitalii nr albumu 268940
# O�wiadczam, �e zadanie wykona�em samodzielnie.

wowels = ["a", "ą", "e", "ę", "i", "o", "ó", "u", "y"]

digits_number = 0
leters_number = 0
vowels_number = 0

text = input("Podaj dowonle zdanie: ")

words = text.split(" ")

for i in text:
    if i.isdigit():
        digits_number += 1
        print(i, "digits:", digits_number)
    elif i.isalpha():
        leters_number += 1
        print(i, "leters:", leters_number)

        if i in wowels:
                vowels_number += 1
                print(i, "vowels:", vowels_number)

print("Liczba słów: ", len(words))
print("Liczba wszystkich liter: ", leters_number)
print("Liczba wszystkich cyfr: ", digits_number)
print("Liczba wszystkich samogłosek: ", vowels_number)