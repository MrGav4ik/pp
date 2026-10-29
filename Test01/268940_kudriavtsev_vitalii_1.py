number1 = input("Podaj pierwszą liczbę rzeczywistą: ")
number2 = input("Podaj drugą liczbę rzeczywistą: ")

if number1.isdigit() == True and number2.isdigit() == True:
    number1 = int(number1)
    number2 = int(number2)

    print(f"{number1} + {number2} = {number1 + number2}")
    print(f"{number1} - {number2} = {number1 - number2}")
    print(f"{number1} * {number2} = {number1 * number2}")
    print(f"Średia aretmetyczna {number1} i {number2} to", (number1 + number2) / 2)
else:
    try:
        number1 = float(number1)
        number2 = float(number2)

        print(f"{number1} + {number2} = {number1 + number2}")
        print(f"{number1} - {number2} = {number1 - number2}")
        print(f"{number1} * {number2} = {number1 * number2}")
        print(f"Średia aretmetyczna {number1} i {number2} to", (number1 + number2) / 2)

    except ValueError:
        print("Podaj liczbę rzeczywistą")
