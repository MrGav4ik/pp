# Laboratorium: 03; Zadanie 06; Autor: Kudriavtsev Vitalii nr albumu 268940
# Oświadczam, że zadanie wykonałem samodzielnie.

print("Równanie kwadratowe ax^2 + bx + c = 0")

a = int(input("Podaj współczynnik a: "))

if a == 0:
    print("Nie jest to równanie kwadratowe")

else:
    b = int(input("Podaj współczynnik b: "))
    c = int(input("Podaj współczynnik c: "))

    delta = (b**2) - (4 * a * c)

    if delta == 0:
        x = int(-b / (2 * a))
        
        print(f"Równanie kwadratowe ma jedno rozwiązanie: x = {x}")

    else:
        delta_sqrt = delta ** 0.5

        x1 = int((-b - delta_sqrt) / (2 * a))
        x2 = int((-b + delta_sqrt) / (2 * a))

        print(f"Równanie kwadratowe ma dwa rozwiązania: x = {x1} oraz x = {x2}")
