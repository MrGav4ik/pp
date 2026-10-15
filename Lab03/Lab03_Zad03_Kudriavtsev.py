# Laboratorium: 03; Zadanie 03; Autor: Kudriavtsev Vitalii nr albumu 262516
# Oświadczam, że zadanie wykonałem samodzielnie.

position = input("Podaj pozycje pola na szachownicy w postaci dwuznaku (np. C1): ")

pos_elements = []

numbers = []

for i in position:
    pos_elements.append(i)

leter = ""

number = ""

for i in range(1, 9):
    numbers.append(i)

for i in pos_elements:
    if i.isdigit() == True:
        number += i
    else:
        leter = i.upper()

print(leter)
print(numbers)

letter_ascii = ord(leter)

# if number is more then one digit e.g. 12 ord() will return TypeError so there's no point to continue as position does't exist
try:
    number_ascii = ord(number)

    sum_ascii = letter_ascii + number_ascii

    if (letter_ascii < ord("A") or letter_ascii > ord("H")) or (number_ascii < ord("1") or number_ascii > ord("8")):
        print("Pole nie istnieje na szachownicy")
    else:
        if sum_ascii % 2 == 0:
            print(f"Podane pole {position} jest czarne")
        else:
            print(f"Podane pole {position} jest białe")

except TypeError:
    print("Pole nie istnieje na szachownicy")
