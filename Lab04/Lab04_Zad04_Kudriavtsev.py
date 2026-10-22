# Laboratorium: 04; Zadanie 04; Autor: Kudriavtsev Vitalii nr albumu 268940
# Oświadczam, że zadanie wykonałem samodzielnie.

value = None
value_int = None
sum = 0
average = 0

numbers = []

while value_int != 0:
    value = input("Podaj liczbę (0 kończy): ")

    if value.isdigit() == True:
        value_int = int(value)
        numbers.append(value_int)
    else:
        try:
            value_float = float(value)
            numbers.append(value_float)
            
        except ValueError:
            print(f'"{value}" nie jest liczbą – pomijam')


numbers.pop()

for i in numbers:
    sum += i

average = sum / len(numbers)

print(f"Podano liczb: {len(numbers)}")
print(f"Suma: {sum}")
print(f"Średnia: {average}")
